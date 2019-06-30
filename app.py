from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/v2/movie/subject/<int:movie_id>')
def hello_world(movie_id):
    if movie_id > 100:
        return jsonify({
            'images': {
                'small': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p616779645.jpg'
            },
            'title': '教父',
            'wish_count': '122658',
            'collect_count': '495811',
            'rating': {
                'average': '9.2'
            },
            'summary': """  40年代的美国，“教父”维托·唐·柯里昂（马龙·白兰度 饰）是黑手党柯里昂家族的首领，带领家族从事非法的勾当，但同时他也是许多弱小平民的保护神，深得人们爱戴。
　　因为拒绝了毒枭索洛索的毒品交易要求，柯里昂家族和纽约其他几个黑手党家族的矛盾激化。圣诞前夕，索洛索劫持了“教 父”的参谋汤姆，并派人暗杀“教父”；因为内奸的出卖，“教父”的大儿子逊尼被仇家杀害；小儿子麦克（阿尔·帕西诺 饰）也被卷了进来，失去爱妻。黑手党家族之间的矛盾越来越白热化。
　　年老的“教父”面对丧子之痛怎样统领全局？黑手党之间的仇杀如何落幕？谁是家族的内奸？谁又能够成为新一代的“教父”？
　　血雨腥风和温情脉脉，在这部里程碑式的黑帮史诗巨片里真实上演。""",
            'msg': '此数据为假数据，仅供小程序入门学习使用'
        })
    else:
        return 404


if __name__ == '__main__':
    app.run()
# 图片images.small
# 标题title
# 想看wish_count
# 看过collect_count
# 评分rating.average
# 简介summary
