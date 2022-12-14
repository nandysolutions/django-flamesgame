from django.shortcuts import render
from django.contrib import messages
from .models import Flames
# Create your views here.
# creator "NANTHAKUMAR J J"
import copy
from collections import Counter


# <!-- Author:  Nanthakumar -->
def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request, exception):
    return render(request, '500.html', status=500)


def home(request):
    f = Flames()
    if request.method == "POST":
        n1 = request.POST.get('n1')
        n2 = request.POST.get('n2')
        str1 = n1
        str2 = n2
        if '.' in str1 or '.' in str2:
            str1 = str1.split('.')
            str2 = str2.split('.')
        else:
            str1 = str1.split()
            str2 = str2.split()
        str1 = [i for i in str1 if len(i) > 1]
        str2 = [i for i in str2 if len(i) > 1]
        str1 = ''.join(str1)
        str2 = ''.join(str2)
        str1 = str1.lower()
        str2 = str2.lower()
        n1 = str1
        n2 = str2
        if len(str(n1)) <= 1 or len(str(n2)) <= 1:
            messages.error(request, "Please ensure that you have given some text in both fields")
            return render(request, 'home.html')
        elif n1 != None and n2 != None:
            if not n1.isalpha() or not n2.isalpha():
                messages.error(request, "Please provide only valid names :(")
                return render(request, 'home.html')
            elif n1 == n2:
                messages.error(request, "We cant guess your relation! Try initials combined with names.")
                return render(request, 'home.html')
        elif n1 is None and n2 is None:
            messages.error(request, "Please ensure that you have given some text in both fields")
            return render(request, 'home.html')
        a = sorted(n1)
        b = sorted(n2)
        freq1 = dict(Counter(a))
        freq2 = dict(Counter(b))
        c = copy.deepcopy(freq1)
        c1 = copy.deepcopy(freq2)
        for (char, count), (char1, count1) in zip(c.items(), c1.items()):
            if len(a) > len(b):
                if char1 in c.keys():
                    freq1[char1] = abs(c1[char1] - c[char1])
                    freq2[char1] = 0
                else:
                    freq2[char1] = 1
            else:
                if char in c1.keys():
                    freq1[char] = abs(c1[char] - c[char])
                    freq2[char] = 0
                else:
                    freq1[char] = 1
        res = sum(freq2.values()) + sum(freq1.values())
        dic = {'F': "Friends", 'L': "Love", 'A': "Affection", 'M': "Marriage", 'E': "Enemy", 'S': "Sister"}
        lst = list(dic.keys())
        for i in range(6, 0, -1):
            r = res % i
            if len(lst) == 1 or len(lst) == 0:
                break
            lst.pop(r - 1)
            if r - 1 > 0:
                lst = lst[r - 1:] + lst[:r - 1]
        final = dic.get(''.join(lst), "No relation")

        f.n1 = n1
        f.n2 = n2
        f.res = str(final)
        if len(str(n1)) != 0 and len(str(n2)) != 0 and str(final) != 'flames':
            f.save()
        return render(request, 'home.html', {'result': final, 'successful_submit': True})
    return render(request, 'home.html')
    # <!-- Author:  Nanthakumar -->
