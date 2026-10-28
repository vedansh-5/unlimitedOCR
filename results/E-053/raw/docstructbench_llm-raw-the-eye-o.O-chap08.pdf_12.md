<|det|>table [104, 82, 825, 201]<|/det|><table><tr><td>Constant</td><td>Value</td><td>Meaning</td></tr><tr><td>kAlertStdAlertOKButton</td><td>1</td><td>The OK push button. The default text for this push button is “OK”.</td></tr><tr><td>kAlertStdAlertCancelButton</td><td>2</td><td>The Cancel push button (optional). The default text for this push button is “Cancel”.</td></tr><tr><td>kAlertStdAlertOtherButton</td><td>3</td><td>A third push button (optional). The default text for this push button is “Don’t Save”.</td></tr><tr><td>kAlertStdAlertHelpButton</td><td>4</td><td>The Help push button (optional).</td></tr></table>
<|det|>title [91, 225, 304, 247]<|/det|>Creating Dialog Boxes
<|det|>text [114, 259, 457, 274]<|/det|>Dialog boxes may be created in one of two ways:
<|det|>text [114, 286, 841, 330]<|/det|>- Using the function GetNewDialog, which takes descriptive information about the dialog from dialog ('DLOG') and extended dialog ('dlgx') resources. The resource ID of the 'DLOG' and 'dlgx' resources must be the same, and is passed in the first parameter of this function.
<|det|>text [114, 342, 840, 371]<|/det|>- Using NewDialog, NewColorDialog, or NewFeaturesDialog, which take descriptive information passed in the parameters of those functions.
<|det|>title [167, 392, 270, 408]<|/det|>Historical Note
<|det|>text [164, 417, 784, 469]<|/det|>The extended dialog resource and the NewFeaturesDialog function were introduced with OS 8 and the Appearance Manager. NewFeaturesDialog should be used to create Appearance-compliant dialogs. Unlike NewDialog and NewColorDialog, it has a flags parameter containing the same flags you would set in an extended dialog resource.
<|det|>text [112, 490, 843, 590]<|/det|>If NULL is specified as the second parameter in the GetNewDialog call, GetNewDialog itself creates a non-relocatable block for the dialog structure. Passing NULL is appropriate for modal and movable modal dialog boxes because you should dispose of the dialog box, and hence the associated dialog structure, when the user dismisses the dialog. However, in order to avoid heap fragmentation effects, you should ordinarily allocate your own memory for modeless dialog box dialog structures (just as you would for a window structure) and specify the pointer to that memory block in the second parameter of the GetNewDialog call.
<|det|>text [112, 601, 841, 631]<|/det|>Regardless of which method is used to create the dialog, a dialog structure and a window structure will be created, and a pointer to the dialog structure will be returned to the calling function.
<|det|>title [92, 641, 267, 661]<|/det|>The Dialog Structure
<|det|>text [113, 673, 782, 689]<|/det|>The dialog structure created by the GetNewDialog call is defined by the data type DialogRecord:
<|det|>text [137, 700, 650, 824]<|/det|>struct DialogRecord
{
    WindowRecord window; // Dialog's window record.
    Handle items; // Item list resource.
    TEHandle text1; // Current editable text item.
    SInt16 editField; // Editable text item number minus 1.
    SInt16 editOpen; // (Used internally.)
    SInt16 adcItem; // Default push button item number.
};
typedef struct DialogRecord DialogRecord;
typedef DialogRecord *DialogPeek;
<|det|>text [112, 834, 840, 863]<|/det|>Note that the dialog structure includes a window structure field. The Dialog Manager sets the windowKind field of this window structure to kDialogWindowKind.
<|det|>page_number [91, 951, 124, 963]<|/det|>8-12
<|det|>footer [205, 951, 279, 963]<|/det|>Version 2.2
<|det|>footer [720, 951, 839, 963]<|/det|>Dialogs and Alerts
