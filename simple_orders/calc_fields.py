from django.forms import Widget, Field, ModelForm, Form
from django.forms.formsets import BaseFormSet
from django.contrib.admin import ModelAdmin
from django.forms.util import flatatt
from django.utils.safestring import mark_safe
from inspect import ismethod
from django.utils.datastructures import MultiValueDictKeyError

class CalcWidget(Widget):
    def __init__(self, format=None, instance=None, attr=None, *args, **kwargs):
        self.format, self.instance, self.attr = format, instance, attr
        super(CalcWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        if self.instance and hasattr(self.instance, self.attr):
            attr = getattr(self.instance, self.attr)
            if ismethod(attr):
                value = attr()
            else:
                value = attr
            if isinstance(self.format, basestring) and self.format:
                value = self.format % value
            return mark_safe(u'<span%s>%s</span>' % (flatatt(self.build_attrs(attrs)),unicode(value),))
        return mark_safe(u'')

class CalcField(Field):
    def __init__(self, format=None, instance=None, attr=None, *args, **kwargs):
        super(CalcField, self).__init__(required=False, \
            widget=CalcWidget(format=format, instance=instance, attr=attr), *args, **kwargs)

    def clean(self, value): #needed?
        return None

class CalcForm(Form):
    calc_defs = None
    def __init__(self, instance=None, *args, **kwargs):
        super(CalcForm, self).__init__(*args, **kwargs)
        self.instance = instance
        if self.calc_defs and isinstance(self.calc_defs, dict):
            for k,v in self.calc_defs.iteritems():
                if isinstance(k, basestring) and isinstance(v, tuple) and len(v) == 2 \
                    and isinstance(v[0], basestring) and isinstance(v[1], basestring):
                        self.fields[k] = CalcField(format=v[1], instance=instance, attr=v[0])

class CalcModelForm(ModelForm):
    calc_defs = None
    def __init__(self, *args, **kwargs):
        super(CalcModelForm, self).__init__(*args, **kwargs)
        if self.calc_defs and isinstance(self.calc_defs, dict):
            for k,v in self.calc_defs.iteritems():
                if isinstance(k, basestring) and isinstance(v, tuple) and len(v) == 2 \
                    and isinstance(v[0], basestring) and isinstance(v[1], basestring):
                        self.fields[k] = CalcField(format=v[1], instance=self.instance, attr=v[0])

class CalcFormSet(BaseFormSet):
    def __init__(self, init_instances=None, *args, **kwargs):
        self.init_instances = init_instances
        super(CalcFormSet, self).__init__(*args, **kwargs)
    def initial_form_count(self):
        if self.init_instances:
            return len(self.init_instances)
        else: return 0
    def _construct_form(self, i, *args, **kwargs):
        if self.init_instances:
            try:
                form = super(CalcFormSet, self)._construct_form(i, instance=self.init_instances[i], *args, **kwargs)
            except (IndexError):
                form = super(CalcFormSet, self)._construct_form(i, *args, **kwargs)
        else:
            form = super(CalcFormSet, self)._construct_form(i, *args, **kwargs)
        return form

class CalcAdmin(ModelAdmin):
    form = CalcModelForm
    calc_defs = None
    calc_fields = None
    _fields = None

    def get_form(self, *args, **kwargs):
        f = super(CalcAdmin, self).get_form(*args, **kwargs)
        f.calc_defs, f.fields = self.calc_defs, self.calc_fields
        return f
    @property
    def fields(self):
        if not self._fields and self.calc_fields:
            if self.calc_defs and isinstance(self.calc_defs, dict):
                self._fields = []
                for field in self.calc_fields:
                    if not field in self.calc_defs:
                        self._fields.append(field)
            else:
                self._fields = self.calc_fields
        return _fields
    @property
    def declared_fieldsets(self):
        if self.fieldsets:
            return self.fieldsets
        elif self.calc_fields:
            return [(None, {'fields': self.calc_fields})]
        return None
    def get_fieldsets(self, request, obj=None):
        # Hook for specifying fieldsets for the add form.
        if self.declared_fieldsets:
            return self.declared_fieldsets
        form = self.get_form(request, obj)()
        return [(None, {'fields': form.fields.keys()})]
