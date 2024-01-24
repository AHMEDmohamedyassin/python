from colored import Fore , Back , Style
from progress.bar import Bar



print(f'{Fore.red}{Back.black}hello colored terminal')

color: str = f'{Style.underline}{Fore.rgb(231 , 245 , 88)}{Back.black}'

print(f'{color} under line with black back ground')
print(Style.reset)


bar = Bar('Processing', max=20 , suffix='%(percent)d%%' , fill='#')
for i in range(2):
    # Do some work
    bar.next()
bar.finish()

