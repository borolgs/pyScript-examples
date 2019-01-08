import clr

clr.AddReference('RevitAPI')
import Autodesk.Revit.DB as DB

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument


def transaction(f, name="", doc=doc):
    def wrapped(*args, **kwargs):
        TransactionManager.Instance.EnsureInTransaction(doc)
        r = f(*args, **kwargs)
        TransactionManager.Instance.TransactionTaskDone()
        return r
    return wrapped




