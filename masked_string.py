return masked string
def maskify(cc):
    cc = list(cc)
    cc[:-4] = ["#"] * 4
    cc = "".join(cc)
    return cc
	
print(maskify("156-7910 748-2167"))

   
cc = ''
r = maskify(cc)
test.describe("masking: {0}".format(cc))
test.it("{0}  matches  {1}".format(cc,r))
test.assert_equals(cc, r)

cc = '123'
r = maskify(cc)
test.describe("masking: {0}".format(cc))
test.it("{0}  matches  {1}".format(cc, r))
test.assert_equals(cc, r)

cc = 'SF$SDfgsd2eA'
r = maskify(cc)
test.describe("masking: {0}".format(cc))
test.it("{0}  matches  {1}".format('########d2eA', r))
test.assert_equals('########d2eA', r)

List comprehensions can contain more complex control flow

