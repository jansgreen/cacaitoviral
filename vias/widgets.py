from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

# THIS CODE COME FROM BOUTIQUE ADO

class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'vias/templates/widgets/clearable_file_input.html'