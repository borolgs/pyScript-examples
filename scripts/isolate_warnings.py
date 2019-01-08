from itertools import chain
from System.Collections.Generic import List
from wrapper import doc, transaction, DB


def get_warning_element_ids():
    warnings = doc.GetWarnings()
    war_elements = list(chain(*(w.GetFailingElements() for w in warnings)))
    return war_elements


@transaction
def isolate_elements(element_ids, view=doc.ActiveView):
    element_to_isolate = List[DB.ElementId](element_ids)
    view.IsolateElementsTemporary(element_to_isolate)


def isolate_warnings():
    warning_el_ids = get_warning_element_ids()
    if not warning_el_ids:
        return "No Warnings"

    isolate_elements(warning_el_ids)
    return "Usolated {} elements".format(len(warning_el_ids))


result = isolate_warnings()
print(result)


