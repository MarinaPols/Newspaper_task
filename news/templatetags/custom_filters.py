import re
from django import template


register = template.Library()

censor = [
   'дурак',
   'лох',
   'тупица',
]


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter(name='censor_aut')
def censor_aut(text):

   if isinstance(text, str):
      cens_text = []
      l_text = text.split()

      while l_text:
         word = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", l_text[0])
         l_word = word.split()

         for i in l_word:
            count = len(l_word) - 1

            if count == 0 and i.lower() in censor:
               bad_word = i[0] + '*' * (len(i) - 1)
               cens_text.append(bad_word)
               break

            if count and i.lower() in censor:
               bad_word = i[0] + '*' * (len(i) - 1)
               g = "".join(l_word)
               res = g.replace(i, bad_word)
               cens_text.append(res)
               break

            if count == 0 and i.lower() not in censor:
               res = "".join(l_word)
               cens_text.append(res)
               break

            if count and i.lower() not in censor:
               res = "".join(l_word)
               cens_text.append(res)
               break

         l_text.remove(l_text[0])

      return " ".join(cens_text)

   else:
      raise TypeError("Фильтр применим только к переменным строкового типа!")