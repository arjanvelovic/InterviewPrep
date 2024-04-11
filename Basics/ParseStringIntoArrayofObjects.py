# Objetive: parse this string into an array of objects:

# ‘Plan,Includes,Price
# Plan A,"one,two,three,four",10
# Plan B,"one,two,three,four",20
# Plan C,"one,two,three,four",30’

# Output:
# const plan = [
#     {
#         plan: ‘Plan A,
#         includes: [‘one’,’two’,’three’, 'four'],
#         price:  ‘$10’
#     },
# ] ;

"""Plan,Includes,Price
Plan A,"one,two,three,four",10
Plan B,"one,two,three,four",20
Plan C,"one,two,three,four",30"""

def Output(string):

    splitLinesArray= string.splitlines()
    # print(splitLinesArray)


    for i in range(1, len(splitLinesArray)):
        LineArray=splitLinesArray[i].split(",")
        
        for j in range(len(LineArray)):
            print(LineArray[j])
            

    # return outDict

Output("""Plan,Includes,Price
Plan A,"one,two,three,four",10
Plan B,"one,two,three,four",20
Plan C,"one,two,three,four",30""")