# VarSet-Update
Rename or change other attributes of existing VarSet properties.

---

## **VarSetUpdate Macro - v0.3.14**

### **Overview**
The v0.3.13 VarSet Property Update Macro is a robust tool for FreeCAD users, streamlining the process of managing and modifying `VarSet` object properties. With its intuitive interface and expression-handling capabilities, this macro ensures seamless updates across FreeCAD documents while preserving object dependencies. The macro is continuously refined to address remaining challenges, including property type transitions and GUI interactions during execution.

---

### **Key Features**
- **Property Renaming**: Safely rename properties within `VarSet` objects, ensuring all dependent expressions and constraints remain intact.
- **Group Reassignment**: Dynamically change the group of a property without breaking references or constraints.
- **Attribute Updates**: Modify property types and tooltips directly through the macro interface.
- **Expression Preservation**: Automatically backs up, clears, and restores expressions referencing modified properties to ensure stability across sketches and objects.
- **Undo-Friendly Transactions**: Encapsulates all changes in FreeCAD transactions, allowing undo functionality for safe experimentation.
- **Dropdown Management**: Intuitive dropdowns let users manually select `VarSet` objects and their properties.
- **Error Logging**: Provides detailed feedback in the results viewer, helping users troubleshoot issues or confirm successful updates.
- **Theme Optimized Colors**: Colors in the macro have been adjusted to work well in both light and dark themes, with easy customization available in the macro code.

---

### **Known Issues**
- **Property Type Transitions**: Changing property types can be challenging due to differences in data requirements. For example, numerical values >360 get truncated when switching to type: Angle. Types like Bool or Enumerated require distinct data structures that complicate transitions.
- **GUI Interaction**: A feature resuest was made to use the current selection at macro initiation During macro execution, users cannot interact with the FreeCAD GUI to select properties, limiting the ability to modify multiple properties in one session.

---

### **Workarounds**
- **Adjusting Colors**: Macro colors can be easily customized in the code. Refer to the comments for guidance on defining colors for light or dark themes.
- **Manual Input for Property Type Transitions**: While changing property types, users might need to manually adjust values to match the destination type. This feature is under review for future improvements.

---

### **System Requirements**
- **FreeCAD Version**: Compatible with v1.1, Python scripting-enabled FreeCAD installations.
- **Objects Supported**: Works with FreeCAD objects containing `VarSet` properties.

---

### **Installation**
1. Clone or download the repository.
2. Place the macro file in your FreeCAD macros directory.
3. Open FreeCAD and load the macro through the `Macros` menu.

---

### **Usage Instructions**
1. **Launch the Macro**:
   - Execute the macro in FreeCAD to open the dialog window.
2. **Select a VarSet and Property**:
   - Use the dropdown menus to manually select a `VarSet` object and property to modify.
   - Attributes of the selected VarSet property will dynamically populate their current values.
3. **Enter Update Details**:
   - Provide the new property name, type, tooltip, or group name in the corresponding fields.
4. **Execute Changes**:
   - Press the update button to apply modifications. The results viewer will display feedback and log any errors or issues.

---

### **Contribute**
Contributions, bug reports, and feature suggestions are welcome! Fork this repository and submit a pull request with your improvements.

---
