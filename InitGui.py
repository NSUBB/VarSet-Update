# InitGui.py
"""
This file initializes the GUI for the VarSet Update addon.
"""

class VarSetUpdateWorkbench:
    def __init__(self):
        self.__class__.MenuText = "VarSet Update"
        self.__class__.ToolTip = "A tool for updating variable sets"
        self.__class__.Icon = "VarSetUpdate.svg"  # Icon path

    def Initialize(self):
        import FreeCADGui
        FreeCADGui.addWorkbench(self)

    def GetClassName(self):
        return "VarSetUpdateWorkbench"

FreeCADGui.addWorkbench(VarSetUpdateWorkbench())
