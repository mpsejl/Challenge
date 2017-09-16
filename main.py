# Parsing libary
import pyparsing

# parse(s):
#
# Parse input string
#
#    Inputs: s - string to parse must use parenthesis for nesting
#                and comma separated alphanumeric fields
#    Output: nested list


def parse(s):
    try:
        nestedexpr = pyparsing.nestedExpr('(', ')')
        nestedlist = nestedexpr.parseString(s).asList()
        return nestedlist[0]  # Return List minus the outer parenthesis
    except pyparsing.ParseException as e:
        print("Error parsing input string:'{}'".format(s))
        print(e)
        raise e
    except Exception as e:
        print("Unexpected Error!\nAborting!")
        raise

# makedict(l, k=None):
#
# Convert nested list output from parse to a Python dictionary
#
#    Input: l - nested list
#           k - starting key (used for recursion)
#    Output: dictionary (all values are None)
#


def makedict(l, k=None):
    d = {}
    for v in l:
        if type(v) == list:
            d[k] = makedict(v)
        else:
            for k in [x.strip() for x in v.split(",")]:
                if len(k) > 0:
                    d[k] = None
    return d


# printNested(d, sort, level)
#
# Print nested tree structure of the input dictionary
# Optioonaly sort keys before printing
#
#    Input: d - Dictionary to print
#           sort - True to sort keys
#           level - Level of tree used for indenting
#
#    Output: Prints Tree to standard Output


def printNested(d, sort=False, level=0):
    keys = list(d)
    if sort:
        keys.sort()
    for key in keys:
        print("{}{} {}".format("  " * level, "-" * level, key))
        if type(d[key]) == dict:
            printNested(d[key], sort, level + 1)


# parseAndPrintString(s, sort)
#
# Parses the input string
# Converts it to a Python dictionary
# Prints the dictionary keys as a nested structure as defined
# by parenthesis in string
#
#     Inputs: s - Input string
#             sort - True to sort by keys when printing
#


def parseAndPrintString(s, sort=False):
    try:
        nestedlist = parse(s)
        d = makedict(nestedlist)
        printNested(d, sort=sort)
        return 0
    except Exception as e:
        return 1


# Run tests


def main():
    test_input = []
    test_input.append("(j,i(h,g(f,e(d,c(b,a)))))")
    test_input.append("(id,created,employee(id,firstname,employeeType(id),lastname),location)")
    
    # Run tests
    for s in test_input:
        print("\n\nProcessing:\n{}\n\nResults:".format(s))
        print("\nWith Unsorted Keys:\n")
        parseAndPrintString(s, sort=False)
        print("\nWith Sorted Keys:\n")
        parseAndPrintString(s, sort=True)

    print("\n\nExiting...\n\n")


main()

#
