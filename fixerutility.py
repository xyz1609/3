import string
import datetime as dt
import codecs

# 1. Removing leading or lagging spaces
print('#1 Removing leading or lagging spaces from a data entry')
baddata = input("Enter a sentence with leading/trailing spaces: ")
print('>', baddata, '<')
cleandata = baddata.strip()
print('>', cleandata, '<')

# 2. Removing nonprintable characters
print('#2 Removing nonprintable characters from a data entry')
baddata_raw = input("Enter a sentence that might include non-printable characters: ")
baddata = codecs.decode(baddata_raw.encode(), 'unicode_escape')
cleandata = ''.join(filter(lambda x: x in string.printable, baddata))
print('Bad Data: ', baddata)
print('Clean Data: ', cleandata)

# 3. Reformatting date entry
print('# 3 Reformatting data entry to match specific formatting criteria.')
baddata = input("Enter a date in YYYY-MM-DD format: ")
try:
    gooddate = dt.datetime.strptime(baddata, '%Y-%m-%d')
    gooddata = format(gooddate, '%d %B %Y')
    print('Bad Data: ', baddata)
    print('Good Data: ', gooddata)
except ValueError:
    print("Invalid date format! Please enter in YYYY-MM-DD format.")


