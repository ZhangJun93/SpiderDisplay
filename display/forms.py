# coding:utf-8
from django import forms

collection_name_list = (
    ("zsyh_spider", '招商银行'),
    ("tzj_spider", "投资界"),
    ("rmw_spider", '人民网金融'),
    ("jqrzj_spider", "机器人之家"),
    ("hsjqr_spider", "华数机器人"),
    ("zhjqr_spider", "中华机器人网"),
)

# collection_name_dict = {
#     "zsyh_spider": '招商银行',
#     "tzj_spider": "投资界",
#      "rmw_spider": '人民网金融',
#      "jqrzj_spider": "机器人之家",
#      "hsjqr_spider": "华数机器人",
#      "zhjqr_spider": "中华机器人网",
# }

class SearchForm(forms.Form):

    # database_name_list = (
    #     (0, "zsyh_spider"),
    #     (1, "tzj_spider"),
    #     (2, "rmw_spider"),
    #     (3, "jqrzj_spider"),
    #     (4, "hsjqr_spider"),
    #     (5, "zhjqr_spider"),
    # )

    CollectionName = forms.CharField(widget=forms.Select(choices=collection_name_list))
    KeyWord = forms.CharField(widget=forms.TextInput(), required=False)  # 可以为空


class DisplayForm(forms.Form):
    key_word = forms.CharField(widget=forms.TextInput())
    collection_name_cn = forms.CharField(widget=forms.TextInput())
    title = forms.CharField(widget=forms.TextInput())
    content = forms.CharField(widget=forms.TextInput())
    date = forms.CharField(widget=forms.TextInput())


if "__name__" == "__main__":
    print(collection_name_list["zhjqr_spider"])