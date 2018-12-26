from django.shortcuts import render, render_to_response
from display.forms import DisplayForm, SearchForm
from display.MongoOperator import MongoOperator
from django.template import RequestContext
from display.utils import find_collectin_name
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from operator import itemgetter

# define database server parameter
ServerIP = '127.0.0.1'
Port = 27017
DataBaseName = 'web_news'
DefaultCollection = "test"
db = MongoOperator(ServerIP, Port, DataBaseName, DefaultCollection)

# Create your views here.


def index(request):
    form = SearchForm()
    return render(request, 'index.html', {'form': form})

results = []
collection_name_cn = ''
key_word = ''


def display(request):
        global results, collection_name_cn, key_word
        per_page = 10
        if request.method == 'POST':
            form = SearchForm(request.POST)

            # if form.is_valid():
            #     data = form.clean()
            data = form.data

            collection_name = data['CollectionName']
            collection_name_cn = find_collectin_name(collection_name)
            key_word = data['KeyWord']
            # print(collection_name, key_word)
            key_word = key_word.strip()
            expression = None
            if key_word != '':
                expression = {"content": {"$regex": key_word}}
            resultItem = db.find(expression=expression, collection_name=collection_name)
            result_count = resultItem.count()
            item_list = []
            for idx, item in enumerate(resultItem):
                # get score
                score = 0
                if len(item["content"].strip()) == 0:
                    continue
                for key in key_word.split("|"):             # multiple keys
                    if key in item['title']:
                        score += 100
                    else:
                        score += item['content'].count(key)
                # content += str(idx) + u"、 标题：" + item['title'] + '\n'
                content = {
                    "title": item['title'],
                    "url": item['url'],
                    'score': score
                }
                item_list.append(content)
            item_list.sort(key=itemgetter('score'), reverse=True)
            for idx in range(len(item_list)):
                item_list[idx]['id'] = idx+1
            results = item_list
            paginator = Paginator(item_list, per_page)
            page = 1
        else:
            page = request.GET.get('page')
            paginator = Paginator(results, per_page)
            result_count = len(results)
        current = page
        try:
            pageInfo = paginator.page(page)
        except PageNotAnInteger:
            pageInfo = paginator.page(1)
            current = 1
        except EmptyPage:
            pageInfo = paginator.page(paginator.num_pages)
            current = paginator.num_pages

        return render(request, 'display.html', {'pageInfo': pageInfo, "count": result_count, "current": pageInfo.number,
                                                "collection_name": collection_name_cn, "key_word": key_word,
                                                "page_range": paginator.page_range})
        # return render(request, 'display.html', locals())

