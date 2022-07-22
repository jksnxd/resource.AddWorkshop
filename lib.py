import re


def write_to_line(fileobj, curline):
    absolve_changelog_link = re.search('(gelog)', curline)
    # I think this might be the cause of whatever problem I am dealing with in terms of duplicaiton.
    absolve_collection_id = re.search('(2270313137)', curline)
    if absolve_changelog_link or absolve_collection_id:
        return
    fileobj.write("resource.AddWorkshop(" + curline[55:] + ")" + "\n")


# IDEA FOR DUPLICATION FIX.
# The reason this enumeration function does not remove the duplicated workshop item links/ids
# is because they do not reside next to each other or their can be more than one duplication.
def check_for_duplication(listobj):
    for index, element in enumerate(listobj): # enumeration over a list obj to try and remove all duplication.
        if index + 1 < len(listobj) and index - 1 >= 0:
            prev_el = str(listobj[index - 1])
            curr_el = str(element)
            next_el = str(listobj[index + 1])
            if prev_el == curr_el:
                listobj.remove(prev_el)
            if next_el == curr_el:
                listobj.remove(next_el)
