import re
import math
import sys, os

cardinals = {}
boolean = 1
def stringtoint(s):
    return int(s)
def stringtofloat(i):
    return float(i)
def floattostring(i):
    return str(i)
# i got the idea of this method from https://docs.python.org/3/library/re.html#regular-expression-examples
def displaymatch(match, n):
    if match is None:
        return None
    else:
        return match.group(n)
#method to put each cardinal player's name in the cardinals dictionary if it doesnt exist and if it does, then go to statsincardinals method which puts each cardinal
#player's bats and hits in a dictionary with respect to their name
def namesincardinals(name,bat,hit):
        boolean = 0
        if name not in cardinals:
            cardinals[name] = [bats, hits]
            boolean = 1
        if boolean==0:
            statsincardinals(name,bat,hit)           
def statsincardinals(name, bat, hit):
        cardinals[name][0] = addbats(cardinals[name][0], bats) 
        cardinals[name][1] = addhits(cardinals[name][1], hits)
        flag=1
def modifiedswap(x, y):
    temp = x
    temp2 = temp+y
    x = temp2
    return x
#method used for adding up total bats for each cardinals player using a modified swap
def addbats(prevbats, newbats):
    previousbats = prevbats
    newbattings = previousbats + newbats
    prevbats = newbattings
    return prevbats
#method used for adding up total hits for each cardinals player using a modified swap
def addhits(prevhits, newhits):
    previoushits = prevhits
    newhittings = previoushits + newhits
    prevhits = newhittings
    return prevhits
#method to make sure all numbers are up to 3 decimal places even if a number is 0.0 or 0.00 or 0, it will still output 0.000
def protectleadingzeros(num):
    protectedval = ('%03.3f' % num)
    return protectedval
if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")
filename = sys.argv[1]
if not os.path.exists(filename):
	sys.exit(f"Error: File '{sys.argv[1]}' not found")

f = open(filename, "r")
#end of citation
def average(x,y):
    return x/y
regex = re
#method to find the desired regular expressions for cardinal player's name, bats and hits and if found, add them to a temporary array
def grouping(regex,n):
    group = []
    n+=1
    name = displaymatch(regex, n)
    group.append(name)
    n+=1
    bats = displaymatch(regex,n)
    bats = stringtofloat(bats)
    group.append(bats)
    n+=1
    hits = displaymatch(regex,n)
    hits = stringtofloat(hits)
    group.append(hits)
    return group
#main function that parses through each line in the file and applies the regular expressions 
for line in f:
    n=0
    regexsearch =regex.compile(r"(\w+ \w+) batted\s(\d)\stimes\swith\s(\d{1})\b").search(line)
    regexmatch =regex.compile(r"(\w+ \w+) batted\s(\d)\stimes\swith\s(\d{1})\b").match(line)
    if (regexsearch is None):
        #in case .search regex method doesnt work, i try an alternate regex statement which uses .match
        if (regexmatch is None):
            continue
        else:
            group = grouping(regexmatch,n)
            namesincardinals(group[0],group[1],group[2])
    else:
        group = grouping(regexsearch,n)
        name = group[0]
        bats = group[1]
        hits = group[2]
        namesincardinals(group[0],group[1],group[2])
f.close()
finalstats ={}
sortedfinalstats={}
#add all appropriate data to final dictionary which has all the stats and names, i start by adding the names
for name in cardinals:
    finalstats[name] = name
averagearray = {}
#find the average and then storing it in an averagearray
for name in cardinals:
    #to avoid division by 0
    if (cardinals[name][0] == 0):
        continue
    else:
        playeraverage = average(cardinals[name][1], cardinals[name][0])
    averagearray[name]=[playeraverage,cardinals[name][1], cardinals[name][0]]
#putting the total bats in finalstats dictionary
for name in cardinals:
    finalstats[name]=cardinals[name][0]
#putting the total hits in finalstats dictionary
for name in cardinals:
    finalstats[name]=cardinals[name][1]
#putting the averages in finalstats dictionary
for name in averagearray:
    getaverage = averagearray[name][0]
    getbats = averagearray[name][1]
    gethits = averagearray[name][2]
    finalstats[name] = [getaverage, getbats, gethits]
#rounding averages to 3 decimal places
for name in finalstats:
    finalstats[name] = round(finalstats[name][0],3)
#lambda function used for sorting,sorted(d.items(), key=lambda x: x[1], reverse=True) https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
sortedfinalstats = sorted(finalstats.items(), key=lambda getaverage:getaverage[1], reverse=True)
#printing the final result
for x in sortedfinalstats:
    finalaverage = protectleadingzeros(x[1])
    finalaverage = floattostring(finalaverage)
    print(x[0] + ": " +  finalaverage)



