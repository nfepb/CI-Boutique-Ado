from django.forms.widgets import ClearableFileInput
# Renaming gettext_lazy with an alias:
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    # Override with our app's values
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
