#TomTom Report Generator Application Automation
'''
Test Feature: F_Report(Input file and report validation)

Test Case ID: TC_18 
Summary: Input file containing empty lines
Expected: Empty lines should not be counted as edits
'''
def TC_18():
    print("TC_18 - Test to validate empty lines in an input file")
    filepath = 'Canada_2017-05-12__13_24_22.txt'

    non_blank_count = 0

    with open(filepath) as infp:
        for line in infp:
            if line.strip(): #Removing blank or empty lines
                non_blank_count += 1

    print 'number of Edits %d' % non_blank_count

'''
Test Feature: F_Report(Input file and report validation)
'''
'''
Test Case ID: TC_19
Summary: Input file containing corrupted texts
Expected: Edit count is not taken from the input file
'''
def TC_19():
    print("TC_19 - Test to validate Input file containing corrupted texts")
    filepath = 'AMS_2017-05-12__13_24_22.txt'
    edit_count = 0

    with open(filepath) as infp:
        for line in infp:
            if line.strip():
                if "added segment" in line:
                    edit_count += 1
                if "move node" in line:
                    edit_count += 1
                if "deleted node" in line:
                    edit_count += 1
    print 'number of Edits %d' % edit_count

'''
The next test script that is planned to cover is validating the parameters for added segment, move node and deleted node
added segment (ID=1243324, type=road, [-84366674, 45876553, -84366698, 45876568])

move node (ID=7746632 from [-84366674, 45876553] to [-84366675, 45876556])

deleted node (ID=887463, type=POI, [-84365563, 458764443])

Validation of ID, type and Decimal Degree
'''    
TC_18()
TC_19()