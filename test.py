import arabic_reshaper

text_to_be_reshaped = 'اللغة العربية رائعة'
reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
print(reshaped_text)

from arabic_reshaper import ArabicReshaper
configuration = {
    'delete_harakat': False,
    'support_ligatures': True,
    'RIAL SIGN': True,  # Replace ر ي ا ل with ﷼
}
reshaper = ArabicReshaper(configuration=configuration)
l1='ل'
l2='ا'
l3='ر'
l4='ي'
text_to_be_reshaped = 'ب ﺭ ﻱ ﺕ' # had to split the string for display
reshaped_text = reshaper.reshape(text_to_be_reshaped.replace(' ',''))
print(reshaped_text)