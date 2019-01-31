"""Collects all analytical lines"""

# import statements-------------------------------------------------
import clr
clr.AddReferenceByPartialName('PresentationCore')
clr.AddReferenceByPartialName("PresentationFramework")
clr.AddReferenceByPartialName('System')
clr.AddReferenceByPartialName('System.Windows.Forms')

from Autodesk.Revit import DB
from Autodesk.Revit import UI

#import Autodesk.Revit.DB as DB

# ------------------------------------------------------------------

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument


element_id = DB.ElementId()
#analytical_model_id = DB.Eleme


print(el.GetAnalyticalModel().GetCurve().GetEndPoint(0))