from itertools import chain
from System.Collections.Generic import List
from wrapper import doc, transaction, DB


def isolate_warnings():
    warning_el_ids = get_warning_element_ids()
    if not warning_el_ids:
        return "No Warnings"

    isolate_elements(warning_el_ids)
    return "Usolated {} elements".format(len(warning_el_ids))


def get_warning_element_ids():
    warnings = doc.GetWarnings()
    element_ids = list(chain(*(w.GetFailingElements() for w in warnings)))
    return element_ids


@transaction
def isolate_elements(element_ids, view=doc.ActiveView):
    elements_to_isolate = List[DB.ElementId](element_ids)
    view.IsolateElementsTemporary(elements_to_isolate)


result = isolate_warnings()
print(result)


