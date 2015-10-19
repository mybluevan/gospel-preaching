from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
def orderurl(field, curorder, page=None):
    if (page == None) or page.number == 1:
        if field == curorder:
            field = ''.join(['-', field])
        return ''.join(['?order=', field])
    else:
        if field == curorder:
            field = ''.join(['-', field])
        return ''.join(['?order=', field, '&page=', page.number])

@register.simple_tag
def pageurl(page, order=None):
    page = str(page)
    if (order == None):
        return ''.join(['?page=', page])
    else:
        return ''.join(['?order=', order, '&page=', page])

@register.simple_tag
def smartpagelinks(pager, page, r, order=None):
    bp = (r * 4) + 3
    out = ''
    page_range = pager.page_range
    num_pages = pager.num_pages
    page_num = page.previous_page_number() + 1

    if num_pages < bp:
        for p in page_range:
            out = ''.join([out, '<a ', ('', 'class="current" ')[p == page_num], 'href="', pageurl(p, order), '">', str(p), '</a> '])
    else:
        if page_num > 1 +(2 * r):
            start = page_num - r
        else:
            start = 1 + r
        if page_num < num_pages - (2 * r):
            end = page_num + r
        else:
            end = num_pages - r

        for p in page_range[0:r]:
            out = ''.join([out, '<a ', ('', 'class="current" ')[p == page_num], 'href="', pageurl(p, order), '">', str(p), '</a> '])
        if page_num > 1 +(2 * r):
            out = ''.join([out, '&hellip; '])
        for p in page_range[start-1:end]:
            out = ''.join([out, '<a ', ('', 'class="current" ')[p == page_num], 'href="', pageurl(p, order), '">', str(p), '</a> '])
        if page_num < num_pages - (2 * r):
            out = ''.join([out, '&hellip; '])
        for p in page_range[num_pages-r:num_pages]:
            out = ''.join([out, '<a ', ('', 'class="current" ')[p == page_num], 'href="', pageurl(p, order), '">', str(p), '</a> '])

    return out

@register.filter
def splitmenu(value, arg):
    app_list = list(value)

    split = int(len(app_list) / 2)
    if len(app_list) % 2:
        split += 1
    left_list = listbalance(app_list[:split], arg, '&nbsp;')
    right_list = listbalance(app_list[split:], arg, '&nbsp;')
    left_list.extend(right_list)
    return left_list

@register.filter
def listbalance(bal_list, length, balance):
    blanks = length - len(bal_list)
    if blanks < 0: blanks = 0
    if blanks % 2:
        bal_list.append(balance)
        blanks -= 1
    if blanks > 0:
        for i in range(blanks / 2):
            bal_list.insert(0, balance)
            bal_list.append(balance)
    return bal_list

@register.simple_tag
def closetag(itemlist, mod, tag):
    if not len(itemlist)%mod == 0:
        return tag
    else:
        return ''

@register.filter
def lt(value, arg):
    return value < arg

@register.filter
def gt(value, arg):
    return value > arg

@register.filter
def eq(value, arg):
    return value == arg

@register.filter
def lte(value, arg):
    return value <= arg

@register.filter
def gte(value, arg):
    return value >= arg

@register.filter
@stringfilter
def startswith(value, arg):
    return value.startswith(arg)
