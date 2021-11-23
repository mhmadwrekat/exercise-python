# add faker Library
from faker import Faker
def view():
    print('-'*30)
fake_en = Faker()
view()
print(fake_en.name())
view()
print(fake_en.first_name())
view()
print('hi')
view()
fake_ar = Faker('ar_PS')
print(fake_ar.name())
view()

content = ''

for i in range(10) :
    temp = ''
    temp += fake_en.paragraph() + '\n'
    temp += fake_en.phone_number() + '\n'
    temp += fake_ar.paragraph() + '\n'
    temp += fake_en.email() + '\n'
    temp += fake_ar.first_name() + '\n'
    temp += fake_en.paragraph() + '\n'
    temp += '-' * 30 + '\n'
    content += temp

with open ('fake_text.txt', 'w') as f :
    f.write(content)

#.Move The File
#import shutil
#shutil .move('fake_text.txt', 'assest')

#.Copy The File
#import shutil
#shutil .copy('fake_text.txt', 'assest')