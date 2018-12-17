import xlrd
book = xlrd.open_workbook("rent_3.xlsx")
sh = book.sheet_by_index(0)

print(sh.nrows)

name = []
cnt = 0
name.append(sh.cell_value(rowx=1, colx=0))
for i in range(1, sh.nrows):
	if sh.cell_value(rowx=i, colx=0) != name[cnt]:
		cnt += 1
		name.append(sh.cell_value(rowx=i, colx=0))

# the information of stations in taipei
a = [
  {
    "StationUID": "TPE0001",
    "StationID": "0001",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運市政府站(3號出口)",
      "En": "MRT Taipei City Hall Stataion(Exit 3)-2"
    },
    "StationPosition": {
      "PositionLat": 25.0408578889,
      "PositionLon": 121.567904444
    },
    "StationAddress": {
      "Zh_tw": "忠孝東路/松仁路(東南側)",
      "En": "The S.W. side of Road Zhongxiao East Road & Road Chung Yan."
    },
    "BikesCapacity": 180,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0002",
    "StationID": "0002",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運國父紀念館站(2號出口)",
      "En": "MRT S.Y.S Memorial Hall Stataion(Exit 2.)"
    },
    "StationPosition": {
      "PositionLat": 25.041254,
      "PositionLon": 121.55742
    },
    "StationAddress": {
      "Zh_tw": "忠孝東路四段/光復南路口(西南側)",
      "En": "Sec,4. Zhongxiao E.Rd/GuangFu S. Rd"
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:36+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0003",
    "StationID": "0003",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "台北市政府",
      "En": "Taipei City Hall"
    },
    "StationPosition": {
      "PositionLat": 25.0377972222,
      "PositionLon": 121.565169444
    },
    "StationAddress": {
      "Zh_tw": "台北市政府東門(松智路) ",
      "En": "Taipei City Government Eastgate (Song Zhi Road)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:36+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0004",
    "StationID": "0004",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "市民廣場",
      "En": "Citizen Square"
    },
    "StationPosition": {
      "PositionLat": 25.0360361111,
      "PositionLon": 121.562325
    },
    "StationAddress": {
      "Zh_tw": "市府路/松壽路(西北側) ",
      "En": "The N.W. side of Road Shifu & Road Song Shou."
    },
    "BikesCapacity": 60,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0005",
    "StationID": "0005",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "興雅國中",
      "En": "Xingya Jr. High School"
    },
    "StationPosition": {
      "PositionLat": 25.0365638889,
      "PositionLon": 121.5686639
    },
    "StationAddress": {
      "Zh_tw": "松仁路/松仁路95巷(東南側)",
      "En": "The S.E. side of Road Songren & Ln. 95, Songren Rd.."
    },
    "BikesCapacity": 60,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0006",
    "StationID": "0006",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北南山廣場",
      "En": "NAN SHAN PLAZA"
    },
    "StationPosition": {
      "PositionLat": 25.034047,
      "PositionLon": 121.565973
    },
    "StationAddress": {
      "Zh_tw": "松智路/松廉路(東北側) ",
      "En": "The N.E. side of Road Song Zhi & Road Song Lian."
    },
    "BikesCapacity": 80,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0007",
    "StationID": "0007",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "信義廣場(台北101)",
      "En": "Xinyi Square(Taipei 101)"
    },
    "StationPosition": {
      "PositionLat": 25.0330388889,
      "PositionLon": 121.565619444
    },
    "StationAddress": {
      "Zh_tw": "松智路/信義路(東北側) ",
      "En": "The N.E. side of Road Song Zhi & Road Xinyi."
    },
    "BikesCapacity": 80,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0008",
    "StationID": "0008",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "世貿三館",
      "En": "TWTC Exhibition Hall 3"
    },
    "StationPosition": {
      "PositionLat": 25.0352138889,
      "PositionLon": 121.563688889
    },
    "StationAddress": {
      "Zh_tw": "市府路/松壽路(東南側) ",
      "En": "The S.E. side of Road Shifu & Road Song Shou."
    },
    "BikesCapacity": 60,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0009",
    "StationID": "0009",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "松德站",
      "En": "Songde"
    },
    "StationPosition": {
      "PositionLat": 25.031785,
      "PositionLon": 121.57448
    },
    "StationAddress": {
      "Zh_tw": "台北市信義區松德路300號",
      "En": "No.300, Songde Rd.(32)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0010",
    "StationID": "0010",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "台北市災害應變中心",
      "En": "Emergency Operations Center of Taipei City"
    },
    "StationPosition": {
      "PositionLat": 25.0286611111,
      "PositionLon": 121.566116667
    },
    "StationAddress": {
      "Zh_tw": "台北市信義區莊敬路391巷11弄2號",
      "En": "No.2, Aly. 11, Ln. 391, Zhuangjing Rd."
    },
    "BikesCapacity": 54,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0011",
    "StationID": "0011",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "三張犁",
      "En": "Sanchangli"
    },
    "StationPosition": {
      "PositionLat": 25.034937,
      "PositionLon": 121.55762
    },
    "StationAddress": {
      "Zh_tw": "光復南路/基隆路一段364巷",
      "En": "The S.E. side of Road Guangfu South & Ln. 346, Sec. 1, Keelung Rd."
    },
    "BikesCapacity": 66,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0012",
    "StationID": "0012",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北醫學大學",
      "En": "Taipei Medical University"
    },
    "StationPosition": {
      "PositionLat": 25.026679,
      "PositionLon": 121.561747
    },
    "StationAddress": {
      "Zh_tw": "台北醫學大學(吳興街220巷59弄)",
      "En": "Aly. 59, Ln. 220, Wuxing St."
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0013",
    "StationID": "0013",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "福德公園",
      "En": "Fude Park"
    },
    "StationPosition": {
      "PositionLat": 25.03809,
      "PositionLon": 121.58367
    },
    "StationAddress": {
      "Zh_tw": "大道路/福德街路口北西側",
      "En": "The N.W. side of Road Dadao & St. Fude."
    },
    "BikesCapacity": 58,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0014",
    "StationID": "0014",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "榮星花園",
      "En": "Rongxing Park"
    },
    "StationPosition": {
      "PositionLat": 25.06424,
      "PositionLon": 121.54037
    },
    "StationAddress": {
      "Zh_tw": "五常街/龍江路口(西南側)",
      "En": "The S.W. side of St.Wuchang & Road Longjiang."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0015",
    "StationID": "0015",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "饒河夜市",
      "En": "Raohe Night Market"
    },
    "StationPosition": {
      "PositionLat": 25.049845,
      "PositionLon": 121.571885
    },
    "StationAddress": {
      "Zh_tw": "八德路/松信路(西南側)",
      "En": "The S.W. side of St.Wuchang & Road Longjiang."
    },
    "BikesCapacity": 60,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0016",
    "StationID": "0016",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "松山家商",
      "En": "Songshan Vocational High School"
    },
    "StationPosition": {
      "PositionLat": 25.036084,
      "PositionLon": 121.579135
    },
    "StationAddress": {
      "Zh_tw": "林口街/福德街(東南側)",
      "En": "The S.E. side of St. Linkou & St. Fude."
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:43+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0017",
    "StationID": "0017",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民生光復路口",
      "En": "Minsheng & Guangfu Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.05862,
      "PositionLon": 121.55514
    },
    "StationAddress": {
      "Zh_tw": "光復北路/民生東路(西北側)",
      "En": "The N.W. side of Road Guangfu S & Road Minsheng E."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0018",
    "StationID": "0018",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北市藝文推廣處",
      "En": "Taipei City Arts Promotion Office"
    },
    "StationPosition": {
      "PositionLat": 25.048268,
      "PositionLon": 121.552278
    },
    "StationAddress": {
      "Zh_tw": "八德路三段25號前",
      "En": "No.25, Sec. 3, Bade Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0019",
    "StationID": "0019",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "象山公園",
      "En": "Xiangshan Park"
    },
    "StationPosition": {
      "PositionLat": 25.02863,
      "PositionLon": 121.56981
    },
    "StationAddress": {
      "Zh_tw": "松仁路153巷17號對面",
      "En": "No.17, Ln. 153, Songren Rd"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:51+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0020",
    "StationID": "0020",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運科技大樓站",
      "En": "MRT Technology Bldg. Sta."
    },
    "StationPosition": {
      "PositionLat": 25.025896,
      "PositionLon": 121.543293
    },
    "StationAddress": {
      "Zh_tw": "科技大樓站對面(復興南路2段西側)",
      "En": "No.235, Sec. 2, Fusing S. Rd."
    },
    "BikesCapacity": 70,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0021",
    "StationID": "0021",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民生敦化路口",
      "En": "Minsheng & Dunhua Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.057985,
      "PositionLon": 121.548982
    },
    "StationAddress": {
      "Zh_tw": "敦化民生路口公車站旁",
      "En": "The side of bus stop- Dunhua Minsheng Intersection."
    },
    "BikesCapacity": 66,
    "SrcUpdateTime": "2018-11-07T09:06:39+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0022",
    "StationID": "0022",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "松山車站",
      "En": "Songshan Rail Sta."
    },
    "StationPosition": {
      "PositionLat": 25.048824,
      "PositionLon": 121.57845
    },
    "StationAddress": {
      "Zh_tw": "松山車站西出口外自行車格內",
      "En": "Bicycle parking lot- West exit in Songshan station"
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0023",
    "StationID": "0023",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "東新國小",
      "En": "Dongxin Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.055074,
      "PositionLon": 121.602798
    },
    "StationAddress": {
      "Zh_tw": "東新國小側門(東明街62號前)",
      "En": "A side entrance of Dongxin Elementery School(front of No. 62, Dongxin St.)"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0024",
    "StationID": "0024",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "信義建國路口",
      "En": "Xinyi & Jianguo Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.03293,
      "PositionLon": 121.53747
    },
    "StationAddress": {
      "Zh_tw": "信義路三段/建國南路二段(西南側)",
      "En": "The N.S. side of Lianyun St. & Sec. 2, Xinyi Rd."
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0025",
    "StationID": "0025",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "永吉松信路口",
      "En": "Yongji & Songxin Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.04543,
      "PositionLon": 121.57205
    },
    "StationAddress": {
      "Zh_tw": "松信路/永吉路南西側人行道",
      "En": "The sidewalk- the S.W. side of Songxin Rd. & Yongji Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0026",
    "StationID": "0026",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運昆陽站(1號出口)",
      "En": "MRT Kunyang Sta. (Exit 1)"
    },
    "StationPosition": {
      "PositionLat": 25.050142,
      "PositionLon": 121.592375
    },
    "StationAddress": {
      "Zh_tw": "捷運昆陽站1號出口外停車場旁",
      "En": "The side of parking lots in the MRT Kunyang station (exit 1)"
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0027",
    "StationID": "0027",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運南港展覽館站(5號出口)",
      "En": "MRT Nangang Exhibition Center Sta. (Exit 5)"
    },
    "StationPosition": {
      "PositionLat": 25.05469,
      "PositionLon": 121.61669
    },
    "StationAddress": {
      "Zh_tw": "研究院路/市民大道(東北側)",
      "En": "The N.E side of Academia Rd. & Shihmin Blvd."
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0028",
    "StationID": "0028",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "五常公園",
      "En": "Wuchang Park"
    },
    "StationPosition": {
      "PositionLat": 25.04814,
      "PositionLon": 121.57467
    },
    "StationAddress": {
      "Zh_tw": "松隆路/虎林街30巷口(西南側)",
      "En": "The S.W side of Songlong Rd. & Hulin St."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:39+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0029",
    "StationID": "0029",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "金山愛國路口",
      "En": "Jinshan & Aiguo Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.03164,
      "PositionLon": 121.52655
    },
    "StationAddress": {
      "Zh_tw": "愛國東路/金山南路(西南側)",
      "En": "The S.W side of Aiguo St. & Jinshan Rd."
    },
    "BikesCapacity": 54,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0030",
    "StationID": "0030",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "基隆長興路口",
      "En": "Keelung & Changxing Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.017054,
      "PositionLon": 121.544352
    },
    "StationAddress": {
      "Zh_tw": "基隆路/長興街(東南側)",
      "En": "The S.W side of Keelung Rd. & Changsing St."
    },
    "BikesCapacity": 74,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0031",
    "StationID": "0031",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "辛亥新生路口",
      "En": "Xinhai & Xinsheng Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.022413,
      "PositionLon": 121.53456
    },
    "StationAddress": {
      "Zh_tw": "辛亥路/新生南路(高架橋下)",
      "En": "Under the bridge- Sinhai Rd. & Shinsheng S. Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0032",
    "StationID": "0032",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運六張犁站",
      "En": "MRT Liuzhangli Sta."
    },
    "StationPosition": {
      "PositionLat": 25.023884,
      "PositionLon": 121.553161
    },
    "StationAddress": {
      "Zh_tw": "捷運出口外和平東路側",
      "En": "The outside of the MRT exit and the side of Heping E. Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0033",
    "StationID": "0033",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中崙高中",
      "En": "Zhonglun High School"
    },
    "StationPosition": {
      "PositionLat": 25.04878,
      "PositionLon": 121.56087
    },
    "StationAddress": {
      "Zh_tw": "八德路四段91巷(中崙高中)旁",
      "En": "The side of Ln. 91, Sec. 4, Bade Rd. ( beside Zhong-Lun High School)"
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0034",
    "StationID": "0034",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運行天宮站(1號出口)",
      "En": "MRT Xingtian Temple Sta. (Exit 1)"
    },
    "StationPosition": {
      "PositionLat": 25.058369,
      "PositionLon": 121.532934
    },
    "StationAddress": {
      "Zh_tw": "捷運行天宮1號出口後方(松江路側)",
      "En": "The side of Songjiang Rd.(the exit 1 of the MRT station of Xingtian Temple)"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0035",
    "StationID": "0035",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運行天宮站(3號出口)",
      "En": "MRT Xingtian Temple Sta. (Exit 3)"
    },
    "StationPosition": {
      "PositionLat": 25.059978,
      "PositionLon": 121.533302
    },
    "StationAddress": {
      "Zh_tw": "捷運行天宮站3號出口站外",
      "En": "The outside of the MRT station of Xingtian Temple."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0036",
    "StationID": "0036",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺大資訊大樓",
      "En": "NTU Information Bldg."
    },
    "StationPosition": {
      "PositionLat": 25.02101,
      "PositionLon": 121.54153
    },
    "StationAddress": {
      "Zh_tw": "辛亥路二段(臺大外語學院外)",
      "En": "Sec. 2, Xinghai Rd. (the outside ofLanguage Center of National Taiwan University)"
    },
    "BikesCapacity": 72,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0037",
    "StationID": "0037",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運東門站(4號出口)",
      "En": "MRT Dongmen Sta. (Exit 4)"
    },
    "StationPosition": {
      "PositionLat": 25.0337,
      "PositionLon": 121.528988
    },
    "StationAddress": {
      "Zh_tw": "信義路/麗水街口",
      "En": "Ren’ai Rd. & Lishuei St. "
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0038",
    "StationID": "0038",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺灣師範大學(圖書館)",
      "En": "NTNU Library"
    },
    "StationPosition": {
      "PositionLat": 25.02665,
      "PositionLon": 121.52889
    },
    "StationAddress": {
      "Zh_tw": "和平東路/師大路口(北側)",
      "En": "The N. side of Heping E. Rd. & Shihda Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0039",
    "StationID": "0039",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南港世貿公園",
      "En": "Nangang Park"
    },
    "StationPosition": {
      "PositionLat": 25.058,
      "PositionLon": 121.61422
    },
    "StationAddress": {
      "Zh_tw": "三重路/經貿二路88巷(東北側)",
      "En": "The N.E. side of Sanchong Rd. & Ln. 88, Jingmao 2nd Rd."
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0040",
    "StationID": "0040",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "玉成公園",
      "En": "Yucheng Park"
    },
    "StationPosition": {
      "PositionLat": 25.04287,
      "PositionLon": 121.5864
    },
    "StationAddress": {
      "Zh_tw": "玉成街247號前",
      "En": "The front of No. 247, Yucheng St."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0041",
    "StationID": "0041",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中研公園",
      "En": "Academia Park"
    },
    "StationPosition": {
      "PositionLat": 25.047425,
      "PositionLon": 121.613706
    },
    "StationAddress": {
      "Zh_tw": "研究院路二段12巷/研究院路二段12巷58弄(西南側)",
      "En": "The S.W side of Ln. 12, Sec. 2, Academia Rd. & Aly. 58, Ln. 12, Sec. 2, Academia Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0042",
    "StationID": "0042",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運後山埤站(1號出口)",
      "En": "MRT Houshanpi Sta.(Exit 1)"
    },
    "StationPosition": {
      "PositionLat": 25.04431,
      "PositionLon": 121.58174
    },
    "StationAddress": {
      "Zh_tw": "中坡北路/忠孝東路五段(西北側)",
      "En": "The S.W side of Jhongsiao E. Rd. & Jhongpo N. Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0043",
    "StationID": "0043",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "凌雲市場",
      "En": "Linyun Market"
    },
    "StationPosition": {
      "PositionLat": 25.035639,
      "PositionLon": 121.614154
    },
    "StationAddress": {
      "Zh_tw": "研究院路三段68巷/凌雲街(東北側)",
      "En": "The N.E. side of St. Lingyun & Academia Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0044",
    "StationID": "0044",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運南港軟體園區站(2號出口)",
      "En": "MRT Nangang Software Park Sta.(Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.05973,
      "PositionLon": 121.616187
    },
    "StationAddress": {
      "Zh_tw": "捷運南港軟體園區站2號出口外",
      "En": "The outside of the MRT station exit 2 of Taipei Nangang Exhibition Center"
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:33+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0045",
    "StationID": "0045",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運公館站(2號出口)",
      "En": "MRT Gongguan Sta.(Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.01476,
      "PositionLon": 121.534538
    },
    "StationAddress": {
      "Zh_tw": "羅斯福路四段/舟山路(東北側)",
      "En": "The N.W. side of Roosevelt Rd.& Sinhai Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0046",
    "StationID": "0046",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南港國小",
      "En": "Nangang Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.05646,
      "PositionLon": 121.611027
    },
    "StationAddress": {
      "Zh_tw": "惠民街/興東街(南側停車場)",
      "En": "The opposite of parking lots of exit Singdong St. (Nan-Gang Elementary School)"
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0047",
    "StationID": "0047",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運忠孝新生站(3號出口)",
      "En": "MRT Zhongxiao Xinsheng Sta.(Exit 3)"
    },
    "StationPosition": {
      "PositionLat": 25.041924,
      "PositionLon": 121.533862
    },
    "StationAddress": {
      "Zh_tw": "捷運忠孝新生站(3號出口)",
      "En": "The intersection of Sec. 3, Zhongxiao E. Rd. & Ln. 10, Sec. 3, Zhongxiao E. Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0048",
    "StationID": "0048",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南港車站(忠孝東路)",
      "En": "Nangang Rail Sta.(Zhongxiao E.Rd.)"
    },
    "StationPosition": {
      "PositionLat": 25.05247,
      "PositionLon": 121.608202
    },
    "StationAddress": {
      "Zh_tw": "忠孝東路七段與忠孝東路七段415巷交叉口",
      "En": "The intersection of Sec. 7, Zhongxiao E. Rd. & Ln. 415, Sec. 7, Zhongxiao E. Rd"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0049",
    "StationID": "0049",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "龍門廣場",
      "En": "Longmen Square"
    },
    "StationPosition": {
      "PositionLat": 25.040901,
      "PositionLon": 121.548252
    },
    "StationAddress": {
      "Zh_tw": "忠孝東路/敦化南路(西南側廣場）",
      "En": "Sec. 1, Dunhua S. Rd. & Ln. 236, Sec. 1, Dunhua S. Rd."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0050",
    "StationID": "0050",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民權運動公園",
      "En": "MinQuan Park"
    },
    "StationPosition": {
      "PositionLat": 25.062002,
      "PositionLon": 121.560186
    },
    "StationAddress": {
      "Zh_tw": "民權東路四段/新中街交叉口",
      "En": "The intersection of Sec. 4, Mincyuan E. Rd. & Xinzhong St."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:37+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0051",
    "StationID": "0051",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "建國農安街口",
      "En": "Jianguo & Nongan Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.065031,
      "PositionLon": 121.536775
    },
    "StationAddress": {
      "Zh_tw": "建國北路/農安街口(中油旁邊空地)",
      "En": "(Behind empty area of CPC coporation) Jianguo N. Rd. & Nong’an St."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0052",
    "StationID": "0052",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "建國長春路口",
      "En": "Jianguo & Changchun Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.054761,
      "PositionLon": 121.536925
    },
    "StationAddress": {
      "Zh_tw": "建國北路/長春路口(北側)",
      "En": "The N. side of Jianguo N. Rd. & Changchun Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0053",
    "StationID": "0053",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "八德市場",
      "En": "Bade Market"
    },
    "StationPosition": {
      "PositionLat": 25.044781,
      "PositionLon": 121.536609
    },
    "StationAddress": {
      "Zh_tw": "建國南路一段/市民大道交叉口(北側) ",
      "En": "The intersection of Sec.1, Jianguo S. Rd. & Civic Blvd."
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:20+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0054",
    "StationID": "0054",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北市立圖書館(總館)",
      "En": "Taipei Public Library"
    },
    "StationPosition": {
      "PositionLat": 25.028798,
      "PositionLon": 121.538073
    },
    "StationAddress": {
      "Zh_tw": "建國南路二段/建國南路二段151巷(東北側)",
      "En": "The N.E. side of Sec. 2, Jianguo S. Rd. & Ln. 151, Sec. 2, Jianguo S. Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0055",
    "StationID": "0055",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北田徑場",
      "En": "Taipei Stadium"
    },
    "StationPosition": {
      "PositionLat": 25.049505,
      "PositionLon": 121.549408
    },
    "StationAddress": {
      "Zh_tw": "敦化北路3號",
      "En": "No.3, Dunhua N. Rd."
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:54+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0056",
    "StationID": "0056",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "仁愛林森路口",
      "En": "Renai & Linsen Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.038954,
      "PositionLon": 121.522334
    },
    "StationAddress": {
      "Zh_tw": "林森南路/仁愛路一段路口(東北側)",
      "En": "The N.E. side of Linsen S. Rd & Sec. 1, Ren’ai Rd.(42)"
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0057",
    "StationID": "0057",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新生和平路口",
      "En": "Xinsheng & Heping Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.026217,
      "PositionLon": 121.53519
    },
    "StationAddress": {
      "Zh_tw": "新生南路二段/和平東路二段(東北側)",
      "En": "The N.E. side of Sec. 2, Xinsheng S. Rd. & Sec. 2, Heping E. Rd"
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0058",
    "StationID": "0058",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運善導寺站(1號出口)",
      "En": "MRT Shandao Temple Sta(Exit 1)"
    },
    "StationPosition": {
      "PositionLat": 25.045267,
      "PositionLon": 121.5222
    },
    "StationAddress": {
      "Zh_tw": "天津街/忠孝東路一段(東北側)",
      "En": "The N.E. side of Tianjin St. & Sec. 1, Zhongxiao E. Rd."
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0059",
    "StationID": "0059",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "林森公園",
      "En": "Linsen Park"
    },
    "StationPosition": {
      "PositionLat": 25.052227,
      "PositionLon": 121.525805
    },
    "StationAddress": {
      "Zh_tw": "林森北路/南京東路一段",
      "En": "Linsen N. Rd. & Sec. 1, Nanjing E. Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:15+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0060",
    "StationID": "0060",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中山行政中心",
      "En": "Zhongshan Dist. Admin. Office"
    },
    "StationPosition": {
      "PositionLat": 25.064317,
      "PositionLon": 121.533487
    },
    "StationAddress": {
      "Zh_tw": "松江路/農安街口",
      "En": "Songjiang Rd. & Nong’an St."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:39+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0061",
    "StationID": "0061",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "台灣科技大學",
      "En": "N.T.U.S.T"
    },
    "StationPosition": {
      "PositionLat": 25.0131,
      "PositionLon": 121.539723
    },
    "StationAddress": {
      "Zh_tw": "基隆路四段/基隆路四段73巷交叉口",
      "En": "The intersection of Sec. 4, Keelung Rd. & Ln. 73, Sec. 4, Keelung Rd"
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0062",
    "StationID": "0062",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南昌公園",
      "En": "Nanchang Park"
    },
    "StationPosition": {
      "PositionLat": 25.026827,
      "PositionLon": 121.520258
    },
    "StationAddress": {
      "Zh_tw": "和平西路一段/南昌路",
      "En": "Sec. 1, Heping W. Rd.& Nanchang Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0063",
    "StationID": "0063",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "仁愛醫院",
      "En": "Taipei City Hospital Renai Branch"
    },
    "StationPosition": {
      "PositionLat": 25.037569,
      "PositionLon": 121.545632
    },
    "StationAddress": {
      "Zh_tw": "大安路一段/仁愛路四段",
      "En": "Da’an Rd. & Sec. 4, Sinyi Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0064",
    "StationID": "0064",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "國家圖書館",
      "En": "National Central Library"
    },
    "StationPosition": {
      "PositionLat": 25.037773,
      "PositionLon": 121.517029
    },
    "StationAddress": {
      "Zh_tw": "中山南路/貴陽街口(西南側)",
      "En": "The S.W. side of Zhongshan S. Rd. & Guiyang St."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0065",
    "StationID": "0065",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "青年公園3號出口",
      "En": "Youth Park(Exit 3)"
    },
    "StationPosition": {
      "PositionLat": 25.022725,
      "PositionLon": 121.502708
    },
    "StationAddress": {
      "Zh_tw": "青年路/青年路106巷(東側)",
      "En": "The E. side of Qingnian Rd. & Ln. 106, Qingnian Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0066",
    "StationID": "0066",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "師範大學公館校區",
      "En": "NTNU Gongguan Campus"
    },
    "StationPosition": {
      "PositionLat": 25.007528,
      "PositionLon": 121.537188
    },
    "StationAddress": {
      "Zh_tw": "師大公館校區校門口(汀州路側)",
      "En": "The side of Tingzhou Rd. (National Taiwan Normal University- Gongguan Campus)"
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0067",
    "StationID": "0067",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運臺大醫院(4號出口)",
      "En": "MRT Nat’l Taiwan U. Hospital Sta.(Exit 4)"
    },
    "StationPosition": {
      "PositionLat": 25.042973,
      "PositionLon": 121.516428
    },
    "StationAddress": {
      "Zh_tw": "公園路/襄陽路(西南側)",
      "En": "The S.W. side of Gongyuan Rd. & Siangyang Rd."
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0068",
    "StationID": "0068",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "國興青年路口",
      "En": "Guoxing & Qingnian Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.025865,
      "PositionLon": 121.506536
    },
    "StationAddress": {
      "Zh_tw": "國興路/青年路(西南側)",
      "En": "The S.W. side of Guoxing Rd. & Qingnian Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0069",
    "StationID": "0069",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "興豐公園",
      "En": "Xingfong Park"
    },
    "StationPosition": {
      "PositionLat": 24.999837,
      "PositionLon": 121.547778
    },
    "StationAddress": {
      "Zh_tw": "興隆路二段123巷/興隆路二段(西北側)",
      "En": "The N.W. side of Ln. 123, Sec. 2, Xinglong Rd. & Sec. 2, Xinglong Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0070",
    "StationID": "0070",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運台北101/世貿站",
      "En": "MRT Taipei 101/World Trade Center Sta."
    },
    "StationPosition": {
      "PositionLat": 25.032752,
      "PositionLon": 121.561645
    },
    "StationAddress": {
      "Zh_tw": "莊敬路/信義路五段(東南側)",
      "En": "The S.E. side of Zhuangjing Rd. & Sec. 5, Xinyi Rd."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0071",
    "StationID": "0071",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運信義安和站(4號出口)",
      "En": "MRT Xinyi Anhe Sta.(Exit.4)"
    },
    "StationPosition": {
      "PositionLat": 25.032985,
      "PositionLon": 121.554204
    },
    "StationAddress": {
      "Zh_tw": "通化街/信義路四段(西南側)",
      "En": "The S.W. side of Tonghua St. & Sec. 4, Xinyi Road., Daan Dist."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0072",
    "StationID": "0072",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新生長安路口",
      "En": "Xinsheng & Changan Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.048611,
      "PositionLon": 121.529346
    },
    "StationAddress": {
      "Zh_tw": "新生北路一段/長安東路二段交叉口(北側)",
      "En": "The intersection of Sec. 1, Xinsheng N. Rd. & Sec. 2, Chang’an E. Rd."
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:36+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0073",
    "StationID": "0073",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "酒泉延平路口",
      "En": "Jiuquan & Yanping Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.072228,
      "PositionLon": 121.510195
    },
    "StationAddress": {
      "Zh_tw": "延平北路四段/酒泉街(西北側)",
      "En": "The N.W. side of Sec. 4, Yanping N. Rd. & Jiuquan St."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0074",
    "StationID": "0074",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "信義連雲街口",
      "En": "Xinyi & Lianyun Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.033817,
      "PositionLon": 121.530547
    },
    "StationAddress": {
      "Zh_tw": "信義路二段/連雲街(東北側)",
      "En": "The N.S. side of Lianyun St. & Sec. 2, Xinyi Rd."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0075",
    "StationID": "0075",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "基隆光復路口",
      "En": "Keelung & Guangfu Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.0300508,
      "PositionLon": 121.557635
    },
    "StationAddress": {
      "Zh_tw": "基隆路二段/光復南路(東北側)",
      "En": "The intersection of Sec. 2, Keelung Rd. & Guangfu S. Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:05:33+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0076",
    "StationID": "0076",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新生長春路口",
      "En": "Xinsheng & Changchun Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.056387,
      "PositionLon": 121.527522
    },
    "StationAddress": {
      "Zh_tw": "新生北路二段/新生北路二段68巷交叉口(新生橋下)",
      "En": "Under the bridge- the intersection of Sec. 2, Xinsheng N. Rd. & Ln. 68, Sec. 2, Xinsheng N. Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:15+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0077",
    "StationID": "0077",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民生活動中心",
      "En": "Minsheng Activity Center"
    },
    "StationPosition": {
      "PositionLat": 25.059147,
      "PositionLon": 121.56297
    },
    "StationAddress": {
      "Zh_tw": "民生東路五段/三民路口(西北側)",
      "En": "The N.W. side of Sec. 5, Minsheng E. Rd. & Sanmin Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0078",
    "StationID": "0078",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運圓山站(2號出口)",
      "En": "MRT Yuanshan Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.071824,
      "PositionLon": 121.519287
    },
    "StationAddress": {
      "Zh_tw": "承德路三段/庫倫街(東南側)",
      "En": "The S.E. side of Sec. 3, Chengde Rd. & Kulun St."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0079",
    "StationID": "0079",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運民權西路站(3號出口)",
      "En": "MRT Minquan W.Rd. Sta.(Exit 3)"
    },
    "StationPosition": {
      "PositionLat": 25.061285,
      "PositionLon": 121.520205
    },
    "StationAddress": {
      "Zh_tw": "民權西路70巷37號對面",
      "En": "The opposite of No.37, Ln. 70, Minquan W. Rd."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:04:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0080",
    "StationID": "0080",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "華江高中",
      "En": "Huajiang High School"
    },
    "StationPosition": {
      "PositionLat": 25.02751,
      "PositionLon": 121.495869
    },
    "StationAddress": {
      "Zh_tw": "東園街/東園街35巷(東北側)",
      "En": "The N.E. side of Dongyuan St. & Ln. 35, Dongyuan St."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:39+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0081",
    "StationID": "0081",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運台電大樓站(2號出口)",
      "En": "MRT Taipower Building Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.020547,
      "PositionLon": 121.528552
    },
    "StationAddress": {
      "Zh_tw": "羅斯福路/辛亥路交叉口(古亭國小前)",
      "En": "The intersection of Roosevelt Rd. & Xinhai Rd. (Gu Ting Elementary School) "
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0082",
    "StationID": "0082",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運西門站(3號出口)",
      "En": "MRT Ximen Sta.(Exit 3)"
    },
    "StationPosition": {
      "PositionLat": 25.041778,
      "PositionLon": 121.508693
    },
    "StationAddress": {
      "Zh_tw": "中華路一段/寶慶路(東南側)",
      "En": "The S.E. side of Sec. 1, Zhonghua Rd. & Baoqing Rd."
    },
    "BikesCapacity": 60,
    "SrcUpdateTime": "2018-11-07T09:06:39+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0083",
    "StationID": "0083",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運大安森林公園站",
      "En": "MRT Daan Park Sta."
    },
    "StationPosition": {
      "PositionLat": 25.033344,
      "PositionLon": 121.534236
    },
    "StationAddress": {
      "Zh_tw": "信義路三段31巷/信義路三段(南側)",
      "En": "The S. side of Ln. 31, Sec. 3, Xinyi Rd. & Sec. 3, Xinyi Rd."
    },
    "BikesCapacity": 74,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0084",
    "StationID": "0084",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "復華花園新城",
      "En": "Fuhua Garden New Village(City)"
    },
    "StationPosition": {
      "PositionLat": 25.029705,
      "PositionLon": 121.502899
    },
    "StationAddress": {
      "Zh_tw": "西藏路115號/西藏路(東南側)",
      "En": "The S.E. side of No.115, Xizang Rd. & Xizang Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:39+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0085",
    "StationID": "0085",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "信義敦化路口",
      "En": "Xinyi & Dunhua Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.033362,
      "PositionLon": 121.54911
    },
    "StationAddress": {
      "Zh_tw": "信義路四段/敦化南路一段(東北側)",
      "En": "The N.E. side of Sec. 4, Xinyi Rd. & Sec. 1, Dunhua S. Rd."
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0086",
    "StationID": "0086",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民權復興路口",
      "En": "Minquan & Fuxing Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.062344,
      "PositionLon": 121.545138
    },
    "StationAddress": {
      "Zh_tw": "復興北路/民權東路三段(東北側)",
      "En": "The N.E. side of Fuxing N. Rd. & Sec. 3, Minquan E. Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0087",
    "StationID": "0087",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運大安站",
      "En": "MRT Daan Sta."
    },
    "StationPosition": {
      "PositionLat": 25.033078,
      "PositionLon": 121.543057
    },
    "StationAddress": {
      "Zh_tw": "復興南路/信義路三段(西南側)",
      "En": "The S.W. side of Fuxing S. Rd. & Sec. 3 Xinyi Rd."
    },
    "BikesCapacity": 22,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0088",
    "StationID": "0088",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運象山站",
      "En": "MRT Xiangshan Sta."
    },
    "StationPosition": {
      "PositionLat": 25.032922,
      "PositionLon": 121.57087
    },
    "StationAddress": {
      "Zh_tw": "信義路五段/信義路五段91巷(西北側)",
      "En": "The N.W. side of Sec. 5, Xinyi Rd. & Ln. 91, Sec. 5, Xinyi Rd."
    },
    "BikesCapacity": 62,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0089",
    "StationID": "0089",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "和平重慶路口",
      "En": "Heping Chongqing Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.027323,
      "PositionLon": 121.516385
    },
    "StationAddress": {
      "Zh_tw": "重慶南路三段/和平西路一段(東北側)",
      "En": "The N.E. side of Sec. 3, Chongqing S. Rd. & Sec. 1, Heping W. Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0090",
    "StationID": "0090",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "老松國小",
      "En": "Laosong Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.037783,
      "PositionLon": 121.501708
    },
    "StationAddress": {
      "Zh_tw": "康定路/桂林路(東南側)",
      "En": "The S.E. side of Kangding Rd. & Guilin Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0091",
    "StationID": "0091",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "市立美術館",
      "En": "Taipei Fine Arts Museum"
    },
    "StationPosition": {
      "PositionLat": 25.070629,
      "PositionLon": 121.523268
    },
    "StationAddress": {
      "Zh_tw": "中山北路三段/酒泉街(西南側)",
      "En": "The S.W. side of Sec. 3, Zhongshan N. Rd. & Jiuquan St."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0092",
    "StationID": "0092",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "開封西寧路口",
      "En": "Kaifong & Xining Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.046618,
      "PositionLon": 121.507169
    },
    "StationAddress": {
      "Zh_tw": "開封街二段/西寧南路(東北側)",
      "En": "The N.E. side of Sec. 2, Kaifeng St. & Xining S. Rd."
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0093",
    "StationID": "0093",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "吳興公車總站",
      "En": "Wu Xing Bus Station."
    },
    "StationPosition": {
      "PositionLat": 25.023877,
      "PositionLon": 121.569836
    },
    "StationAddress": {
      "Zh_tw": "松仁路/吳興街交叉口",
      "En": "The intersection of Songren Rd. & Wuxing St."
    },
    "BikesCapacity": 56,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0094",
    "StationID": "0094",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運景美站",
      "En": "MRT Jingmei Sta."
    },
    "StationPosition": {
      "PositionLat": 24.993254,
      "PositionLon": 121.541059
    },
    "StationAddress": {
      "Zh_tw": "羅斯福路六段/景中街交叉口(東北側)",
      "En": "The intersectionof Sec. 6, Roosevelt Rd. & Jingzhong St."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0095",
    "StationID": "0095",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "東園國小",
      "En": "Dongyuan Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.023393,
      "PositionLon": 121.497679
    },
    "StationAddress": {
      "Zh_tw": "東園街/萬大路344巷(東南側)",
      "En": "The S.E. side of Dongyuan St. & Ln. 344, Wanda Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0096",
    "StationID": "0096",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "三民公園",
      "En": "Sanmin Park"
    },
    "StationPosition": {
      "PositionLat": 25.061567,
      "PositionLon": 121.566558
    },
    "StationAddress": {
      "Zh_tw": "撫遠街/富錦街(東南側)",
      "En": "The S.E. side of Fuyuan St. & Fujin St."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:37+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0097",
    "StationID": "0097",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運劍潭站(2號出口)",
      "En": "MRT Jiantan Sta.(Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.082825,
      "PositionLon": 121.524721
    },
    "StationAddress": {
      "Zh_tw": "基河路18號對面",
      "En": "The opposite of No.18, Jihe Rd."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0098",
    "StationID": "0098",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "羅斯福景隆街口",
      "En": "Roosevelt & Jinglong Intersection"
    },
    "StationPosition": {
      "PositionLat": 24.999378,
      "PositionLon": 121.540197
    },
    "StationAddress": {
      "Zh_tw": "羅斯福路六段/景隆街交叉口(東南側)",
      "En": "The intersection of Sec. 6, Roosevelt Rd. & Jinglong St. (the S.E. side)"
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0099",
    "StationID": "0099",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運雙連站(2號出口)",
      "En": "MRT Shuanglian Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.057866,
      "PositionLon": 121.520711
    },
    "StationAddress": {
      "Zh_tw": "民生西路/萬全街(東北側)",
      "En": "The N.E. side of Minsheng W. Rd. & Wanquan St."
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0100",
    "StationID": "0100",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "金山市民路口",
      "En": "Jinshen & Civic Blvd. Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.045753,
      "PositionLon": 121.530697
    },
    "StationAddress": {
      "Zh_tw": "金山北路/市民大道三段(南側)",
      "En": "The S. side of Jinshan N. Rd. & Sec. 3, Civic Blvd."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0101",
    "StationID": "0101",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "華山文創園區",
      "En": "Huashan 1914‧Creative Park"
    },
    "StationPosition": {
      "PositionLat": 25.043668,
      "PositionLon": 121.528487
    },
    "StationAddress": {
      "Zh_tw": "忠孝東路二段41號前",
      "En": "Front of No.41, Sec. 2, Zhongxiao E. Rd."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:43+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0102",
    "StationID": "0102",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北市客家文化主題公園",
      "En": "Taipei City Hakka Cultural Park"
    },
    "StationPosition": {
      "PositionLat": 25.02043,
      "PositionLon": 121.525322
    },
    "StationAddress": {
      "Zh_tw": "師大路/汀州路交叉口",
      "En": "The intersection of Shida Rd. & Tingzhou Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0103",
    "StationID": "0103",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "萬華車站",
      "En": "Wanhua Rail Sta."
    },
    "StationPosition": {
      "PositionLat": 25.033639,
      "PositionLon": 121.503028
    },
    "StationAddress": {
      "Zh_tw": "艋舺大道83號(對側)",
      "En": "No.83, Bangka Blvd. (oppsite)"
    },
    "BikesCapacity": 60,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0104",
    "StationID": "0104",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "台北花木批發市場",
      "En": "Taipei Pot Plant Auction"
    },
    "StationPosition": {
      "PositionLat": 25.004023,
      "PositionLon": 121.54074
    },
    "StationAddress": {
      "Zh_tw": "萬盛街/興隆路一段(西北側)",
      "En": "The N.W. side of Wansheng St. Sec. 1, Xinglong Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0105",
    "StationID": "0105",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "峨嵋停車場",
      "En": "Emei Parking Lot"
    },
    "StationPosition": {
      "PositionLat": 25.044412,
      "PositionLon": 121.505409
    },
    "StationAddress": {
      "Zh_tw": "昆明街/西寧南路50巷(東南側)",
      "En": "The S.E. side of Kunming St. & Ln. 50, Xining S. Rd. "
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0106",
    "StationID": "0106",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "西園艋舺路口",
      "En": "Xiyuan & Bangka Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.032932,
      "PositionLon": 121.497674
    },
    "StationAddress": {
      "Zh_tw": "西園路二段/艋舺大道(西南側)",
      "En": "The S.W. side of Sec. 2, Xiyuan Rd. & Bangka Blvd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0107",
    "StationID": "0107",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運小南門站(1號出口)",
      "En": "MRT Xiaonanmen Sta. (Exit 1)"
    },
    "StationPosition": {
      "PositionLat": 25.036402,
      "PositionLon": 121.509422
    },
    "StationAddress": {
      "Zh_tw": "博愛路/愛國西路交叉口(西北側)",
      "En": "The intersection of Bo’ai Rd. & Aiguo W. Rd."
    },
    "BikesCapacity": 54,
    "SrcUpdateTime": "2018-11-07T09:06:59+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0108",
    "StationID": "0108",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北孔廟",
      "En": "Taipei Confucius Temple"
    },
    "StationPosition": {
      "PositionLat": 25.073306,
      "PositionLon": 121.515843
    },
    "StationAddress": {
      "Zh_tw": "哈密街59巷/哈密街(東北側)",
      "En": "The N.E. side of Ln. 59, Hami St. & Hami St."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0109",
    "StationID": "0109",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "林安泰古厝",
      "En": "Lin An-tai Historical House"
    },
    "StationPosition": {
      "PositionLat": 25.071606,
      "PositionLon": 121.530805
    },
    "StationAddress": {
      "Zh_tw": "吉林路/民族東路(北側)",
      "En": "The N. side of Jilin Rd. & Minzu E. Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0110",
    "StationID": "0110",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "文湖國小",
      "En": "Wenhu Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.086376,
      "PositionLon": 121.560888
    },
    "StationAddress": {
      "Zh_tw": "文湖街21巷/文湖街(東北側)",
      "En": "The N.E. side of Ln. 21, Wenhu St. & Wenhu St."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0111",
    "StationID": "0111",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運忠孝復興站(2號出口)",
      "En": "MRT Zhongxiao Fuxing Sta.(Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.040184,
      "PositionLon": 121.543497
    },
    "StationAddress": {
      "Zh_tw": "復興南路一段/仁愛路三段123巷13弄(西北側)",
      "En": "The N.W. side of Sec. 1, Fuxing S. Rd. & Aly. 13, Ln. 123, Sec. 3, Ren’ai Rd."
    },
    "BikesCapacity": 54,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0112",
    "StationID": "0112",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運新北投站",
      "En": "MRT Xinbeitou Sta."
    },
    "StationPosition": {
      "PositionLat": 25.137456,
      "PositionLon": 121.503124
    },
    "StationAddress": {
      "Zh_tw": "大業路/中和街交叉口",
      "En": "Daye Rd. & Zhonghe St.  Intersection"
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0113",
    "StationID": "0113",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "仁愛逸仙路口",
      "En": "Renai & Yixian Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.037724,
      "PositionLon": 121.561178
    },
    "StationAddress": {
      "Zh_tw": "仁愛路四段/逸仙路(西北側)",
      "En": "Sec. 4, Ren’ai Rd. & Yixian Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0114",
    "StationID": "0114",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "蘭雅公園",
      "En": "Lanya Park"
    },
    "StationPosition": {
      "PositionLat": 25.109908,
      "PositionLon": 121.530386
    },
    "StationAddress": {
      "Zh_tw": "忠誠路二段/忠誠路二段40巷(西南側)",
      "En": "Sec. 2, Zhongcheng Rd. & Ln. 40, Sec. 2, Zhongcheng Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0115",
    "StationID": "0115",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北轉運站",
      "En": "Taipei Bus Sta."
    },
    "StationPosition": {
      "PositionLat": 25.048222,
      "PositionLon": 121.520526
    },
    "StationAddress": {
      "Zh_tw": "中山北路一段/市民大道一段(西北側)",
      "En": "Sec. 1, Zhongshan N. Rd. & Sec. 1, Civic Blvd."
    },
    "BikesCapacity": 68,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0116",
    "StationID": "0116",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "福林公園",
      "En": "Fulin Park"
    },
    "StationPosition": {
      "PositionLat": 25.096122,
      "PositionLon": 121.530215
    },
    "StationAddress": {
      "Zh_tw": "志成街/中正路(南側)",
      "En": "Zhicheng St. & Zhongzheng Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0117",
    "StationID": "0117",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運北投站",
      "En": "MRT Beitou Sta."
    },
    "StationPosition": {
      "PositionLat": 25.132581,
      "PositionLon": 121.498618
    },
    "StationAddress": {
      "Zh_tw": "光明路2巷/光明路交叉口",
      "En": "Ln. 2, Guangming Rd. & Guangming Rd.  Intersection"
    },
    "BikesCapacity": 58,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0118",
    "StationID": "0118",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "大業大同街口",
      "En": "Daye & Datong Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.136929,
      "PositionLon": 121.499152
    },
    "StationAddress": {
      "Zh_tw": "大業路/大同街口",
      "En": "Daye Rd. & Datong St.  Intersection"
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0119",
    "StationID": "0119",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運劍南路站(2號出口)",
      "En": "MRT Jiannan Rd. Sta.(Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.08418,
      "PositionLon": 121.555116
    },
    "StationAddress": {
      "Zh_tw": "敬業二路/植福路(東北側)",
      "En": "Jingye 2nd Rd. & Zhifu Rd."
    },
    "BikesCapacity": 68,
    "SrcUpdateTime": "2018-11-07T09:06:47+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0120",
    "StationID": "0120",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運龍山寺站(1號出口)",
      "En": "MRT Longshan Temple Sta. (Exit. 1)"
    },
    "StationPosition": {
      "PositionLat": 25.035479,
      "PositionLon": 121.50026
    },
    "StationAddress": {
      "Zh_tw": "和平西路三段/和平西路三段109巷(西北側)",
      "En": "Sec. 3, Heping W. Rd. & Ln. 109, Sec. 3, Heping W. Rd."
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:52+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0121",
    "StationID": "0121",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "龍江南京路口",
      "En": "Longjiang & Nanjing Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.05298,
      "PositionLon": 121.540568
    },
    "StationAddress": {
      "Zh_tw": "龍江路110號對面停車場",
      "En": "No.100, Longjiang Rd."
    },
    "BikesCapacity": 66,
    "SrcUpdateTime": "2018-11-07T09:06:51+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0122",
    "StationID": "0122",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運港墘站(2號出口)",
      "En": "MRT Gangqian Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.079666,
      "PositionLon": 121.57584
    },
    "StationAddress": {
      "Zh_tw": "內湖路一段/港墘路(東南側)",
      "En": "Sec. 1, Neihu Rd./Gangqian Rd. (southeast)"
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:58+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0123",
    "StationID": "0123",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "天母運動公園",
      "En": "Tienmu Sports Park"
    },
    "StationPosition": {
      "PositionLat": 25.116325,
      "PositionLon": 121.534136
    },
    "StationAddress": {
      "Zh_tw": "忠誠路二段/忠誠路二段207巷(東南側)",
      "En": "Sec.2,Zhongcheng Rd./Ln.207,Sec.2,Zhongcheng Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0124",
    "StationID": "0124",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "振華公園",
      "En": "Zenhua Park"
    },
    "StationPosition": {
      "PositionLat": 25.115863,
      "PositionLon": 121.518163
    },
    "StationAddress": {
      "Zh_tw": "振華街36號對面",
      "En": "No.36, Zhenhua St."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0125",
    "StationID": "0125",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "華西公園",
      "En": "Huaxi Park"
    },
    "StationPosition": {
      "PositionLat": 25.038609,
      "PositionLon": 121.498495
    },
    "StationAddress": {
      "Zh_tw": "華西街/桂林路(東北側)",
      "En": "Huaxi St. & Guilin Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0126",
    "StationID": "0126",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "敦化基隆路口",
      "En": "Dunhua & Keelung Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.022073,
      "PositionLon": 121.548336
    },
    "StationAddress": {
      "Zh_tw": "敦化南路二段/基隆路二段交叉口",
      "En": "Sec. 2, Dunhua S. Rd. & Sec. 2, Keelung Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0127",
    "StationID": "0127",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "東湖國中",
      "En": "Donghu Junior High School"
    },
    "StationPosition": {
      "PositionLat": 25.073277,
      "PositionLon": 121.619521
    },
    "StationAddress": {
      "Zh_tw": "康樂街/康樂街125巷(東南側)",
      "En": "Kangle St./Ln. 125, Kangle St."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0128",
    "StationID": "0128",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "成功國宅",
      "En": "Chengong Public Housing"
    },
    "StationPosition": {
      "PositionLat": 25.026808,
      "PositionLon": 121.546726
    },
    "StationAddress": {
      "Zh_tw": "四維路198巷/和平東路三段1巷",
      "En": "Ln. 198, Siwei Rd./Ln. 1, Sec. 3, Heping E. Rd"
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0129",
    "StationID": "0129",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運文德站(2號出口)",
      "En": "MRT Wende Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.078424,
      "PositionLon": 121.58456
    },
    "StationAddress": {
      "Zh_tw": "文德路220巷/文德路(西南側)",
      "En": "Ln. 220, Wende Rd./Wende Rd."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0130",
    "StationID": "0130",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "羅斯福寧波東街口",
      "En": "Roosevelt & Ningbo E. St. Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.031445,
      "PositionLon": 121.519411
    },
    "StationAddress": {
      "Zh_tw": "羅斯福路一段/寧波東街(東南側)",
      "En": "Sec. 1, Roosevelt Rd. & Ningbo E. St."
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0131",
    "StationID": "0131",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "洲子二號公園",
      "En": "Zhouzhi Park No.2"
    },
    "StationPosition": {
      "PositionLat": 25.079322,
      "PositionLon": 121.568688
    },
    "StationAddress": {
      "Zh_tw": "瑞光路500號對面",
      "En": "Opposite to the parking space No.500, Ruiguang Rd."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0132",
    "StationID": "0132",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "羅斯福新生南路口",
      "En": "Roosevelt & Xinsheng S. Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.01603085,
      "PositionLon": 121.5331757
    },
    "StationAddress": {
      "Zh_tw": "羅斯福路四段/新生南路三段交叉口",
      "En": "Sec. 4, Roosevelt Rd./Sec. 3, Xinsheng S. Rd."
    },
    "BikesCapacity": 88,
    "SrcUpdateTime": "2018-11-07T09:05:37+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0133",
    "StationID": "0133",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "蘭興公園",
      "En": "Lanxing Park"
    },
    "StationPosition": {
      "PositionLat": 25.111839,
      "PositionLon": 121.525888
    },
    "StationAddress": {
      "Zh_tw": "中山北路六段/士東路(西北側)",
      "En": "Sec.6, Zhongshan N. Rd / Shidong Rd"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:20+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0134",
    "StationID": "0134",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運芝山站(2號出口)",
      "En": "MRT Zhishan Sta.(Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.10336,
      "PositionLon": 121.522629
    },
    "StationAddress": {
      "Zh_tw": "福華路/福華路162巷(東南側)",
      "En": "Fuhua Rd. / Ln. 162, Fuhua Rd."
    },
    "BikesCapacity": 64,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0135",
    "StationID": "0135",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運石牌站(2號出口)",
      "En": "MRT Shipai Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.114513,
      "PositionLon": 121.515677
    },
    "StationAddress": {
      "Zh_tw": "東華街一段/裕民二路(西側)",
      "En": "Sec. 1, Donghua St. / Yumin 2nd Rd."
    },
    "BikesCapacity": 54,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0136",
    "StationID": "0136",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "國立臺北護理健康大學",
      "En": "NTUNHS"
    },
    "StationPosition": {
      "PositionLat": 25.118049,
      "PositionLon": 121.517512
    },
    "StationAddress": {
      "Zh_tw": "石牌路二段130巷/石牌路二段(東南側)",
      "En": "Ln. 130, Sec. 2, Shipai Rd. / Sec. 2, Shipai Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:37+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0137",
    "StationID": "0137",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "國防大學",
      "En": "Nat’l Defense U."
    },
    "StationPosition": {
      "PositionLat": 25.137976,
      "PositionLon": 121.493066
    },
    "StationAddress": {
      "Zh_tw": "中央北路二段/豐年路二段交叉口",
      "En": "Sec. 2, Zhongyang N. Rd. / Sec. 2, Fengnian Rd."
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0138",
    "StationID": "0138",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運永春站(2號出口)",
      "En": "MRT Yongchun Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.040558,
      "PositionLon": 121.575372
    },
    "StationAddress": {
      "Zh_tw": "忠孝東路五段420號旁(東側巷道上)",
      "En": "No.420, Sec. 5, Zhongxiao E. Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0139",
    "StationID": "0139",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "永樂市場",
      "En": "Yongle Market"
    },
    "StationPosition": {
      "PositionLat": 25.054501,
      "PositionLon": 121.510549
    },
    "StationAddress": {
      "Zh_tw": "民樂街/南京西路233巷(西北側)",
      "En": "Minle St., Datong Dist./Ln. 233, Nanjing W. Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0140",
    "StationID": "0140",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運大橋頭站(2號出口)",
      "En": "MRT Daqiaotou Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.063404,
      "PositionLon": 121.512909
    },
    "StationAddress": {
      "Zh_tw": "民權西路/重慶北路三段(東北側)",
      "En": "Minquan W. Rd./ Sec. 3, Chongqing N. Rd."
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0141",
    "StationID": "0141",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "文山行政中心",
      "En": "Wenshan Dist. Admin. Center"
    },
    "StationPosition": {
      "PositionLat": 24.989902,
      "PositionLon": 121.569984
    },
    "StationAddress": {
      "Zh_tw": "木柵路三段220號前",
      "En": "No.220, Sec. 3, Muzha Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0142",
    "StationID": "0142",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運木柵站",
      "En": "MRT Muzha Sta."
    },
    "StationPosition": {
      "PositionLat": 24.997747,
      "PositionLon": 121.574214
    },
    "StationAddress": {
      "Zh_tw": "木柵路四段82巷18號前(捷運橋樑下)",
      "En": "No.18, Ln. 82, Sec. 4, Muzha Rd."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T08:40:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0143",
    "StationID": "0143",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運動物園站(2號出口)",
      "En": "MRT Taipei Zoo Sta.(Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 24.997659,
      "PositionLon": 121.578752
    },
    "StationAddress": {
      "Zh_tw": "新光路二段28號前",
      "En": "No.28, Sec. 2, Xinguang Rd."
    },
    "BikesCapacity": 72,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0144",
    "StationID": "0144",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "國立政治大學",
      "En": "Nat’l Chengchi U."
    },
    "StationPosition": {
      "PositionLat": 24.988363,
      "PositionLon": 121.576536
    },
    "StationAddress": {
      "Zh_tw": "萬壽路16巷6號前",
      "En": "No.6, Ln. 16, Wanshou Rd."
    },
    "BikesCapacity": 70,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0145",
    "StationID": "0145",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "樹德公園",
      "En": "Shude Park"
    },
    "StationPosition": {
      "PositionLat": 25.066688,
      "PositionLon": 121.516149
    },
    "StationAddress": {
      "Zh_tw": "大龍街/大龍街85巷(東北側)",
      "En": "Dalong St. / Ln. 85, Dalong St."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0146",
    "StationID": "0146",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運士林站(2號出口)",
      "En": "MRT Shilin Sta.(Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.092546,
      "PositionLon": 121.526556
    },
    "StationAddress": {
      "Zh_tw": "中正路247巷/中山北路五段505巷(東南側)",
      "En": "Ln. 247, Zhongzheng Rd. / Ln. 505, Sec. 5, Zhongshan N. Rd."
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0147",
    "StationID": "0147",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "士林運動中心",
      "En": "Shilin Sports Center"
    },
    "StationPosition": {
      "PositionLat": 25.089175,
      "PositionLon": 121.521814
    },
    "StationAddress": {
      "Zh_tw": "承德路四段/大南路(東北側)",
      "En": "Sec. 4, Chengde Rd./Danan Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:33+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0148",
    "StationID": "0148",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運明德站",
      "En": "MRT Mingde Sta."
    },
    "StationPosition": {
      "PositionLat": 25.110331,
      "PositionLon": 121.518316
    },
    "StationAddress": {
      "Zh_tw": "致遠一路一段46巷/西安街一段(東南側)",
      "En": "Ln. 46, Sec. 1, Zhiyuan 1st Rd./Sec. 1, Xi’an St."
    },
    "BikesCapacity": 68,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0149",
    "StationID": "0149",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "北投運動中心",
      "En": "Beitou Sports Center"
    },
    "StationPosition": {
      "PositionLat": 25.116665,
      "PositionLon": 121.509621
    },
    "StationAddress": {
      "Zh_tw": "石牌路一段39巷100號前",
      "En": "No.100, Ln. 39, Sec. 1, Shipai Rd."
    },
    "BikesCapacity": 62,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0150",
    "StationID": "0150",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "松德公園",
      "En": "Songde Park"
    },
    "StationPosition": {
      "PositionLat": 25.036568,
      "PositionLon": 121.57343
    },
    "StationAddress": {
      "Zh_tw": "松德路168巷20號前",
      "En": "No.20, Ln. 168, Songde Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0151",
    "StationID": "0151",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "考試院",
      "En": "Examination Yuan"
    },
    "StationPosition": {
      "PositionLat": 24.987507,
      "PositionLon": 121.549827
    },
    "StationAddress": {
      "Zh_tw": "試院路(雙號)/木柵路一段(東北側)",
      "En": "Shiyuan Rd. / Sec. 1, Muzha Rd., "
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0152",
    "StationID": "0152",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "百齡國小",
      "En": "Bailing Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.08521,
      "PositionLon": 121.519175
    },
    "StationAddress": {
      "Zh_tw": "前港街100巷/前港街(北方)",
      "En": "Ln. 100, Qiangang St. / Qiangang St."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0153",
    "StationID": "0153",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "蔣渭水紀念公園",
      "En": "Jiang Wei-shui Memorial Park"
    },
    "StationPosition": {
      "PositionLat": 25.059885,
      "PositionLon": 121.516299
    },
    "StationAddress": {
      "Zh_tw": "錦西街51號對面",
      "En": "No.51, Jinxi St., Datong Dist."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0154",
    "StationID": "0154",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中正基河路口",
      "En": "Zhongzheng & Jihe Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.093396,
      "PositionLon": 121.519867
    },
    "StationAddress": {
      "Zh_tw": "中正路420號前",
      "En": "No.420, Zhongzheng Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:39+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0155",
    "StationID": "0155",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "瑞光港墘路口",
      "En": "Ruiguang & Gangqian Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.076193,
      "PositionLon": 121.57505
    },
    "StationAddress": {
      "Zh_tw": "瑞光路/港墘路(西南側)",
      "En": "Ruiguang Rd. / Gangqian Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0156",
    "StationID": "0156",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "東湖國小",
      "En": "Donghu Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.06853,
      "PositionLon": 121.61538
    },
    "StationAddress": {
      "Zh_tw": "東湖路/東湖路119巷(西北側)",
      "En": "Donghu Rd. / Ln. 119, Donghu Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0157",
    "StationID": "0157",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "麗山國小",
      "En": "Lishan Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.082703,
      "PositionLon": 121.571467
    },
    "StationAddress": {
      "Zh_tw": "內湖路一段411巷/內湖路一段411巷19弄(東北側)",
      "En": "Ln. 411, Sec. 1, Neihu Rd. / Aly. 19, Ln. 411, Sec. 1, Neihu Rd."
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0158",
    "StationID": "0158",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運東湖站",
      "En": "MRT Donghu Sta."
    },
    "StationPosition": {
      "PositionLat": 25.067026,
      "PositionLon": 121.61355
    },
    "StationAddress": {
      "Zh_tw": "安康路315巷/五分街14巷(西側)",
      "En": "Ln. 315, Ankang Rd./Ln. 14, Wufen St."
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0159",
    "StationID": "0159",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運西湖站(1號出口)",
      "En": "MRT Xihu Sta. (Exit 1)"
    },
    "StationPosition": {
      "PositionLat": 25.082866,
      "PositionLon": 121.566695
    },
    "StationAddress": {
      "Zh_tw": "環山路一段9巷/內湖路一段285巷(西南側)",
      "En": "Ln. 9, Sec. 1, Huanshan Rd./Ln. 285, Sec. 1, Neihu Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:07:01+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0161",
    "StationID": "0161",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "大豐公園",
      "En": "Dafong Park"
    },
    "StationPosition": {
      "PositionLat": 25.131143,
      "PositionLon": 121.503768
    },
    "StationAddress": {
      "Zh_tw": "磺港路/大興街(東北側)",
      "En": "Huanggang Rd. / Daxing St."
    },
    "BikesCapacity": 56,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0162",
    "StationID": "0162",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運中山國小站(4號出口)",
      "En": "MRT Zhongshan Elementary School sta.(Exit 4)"
    },
    "StationPosition": {
      "PositionLat": 25.062924,
      "PositionLon": 121.52772
    },
    "StationAddress": {
      "Zh_tw": "民權東路一段/新生北路三段(北側)(新生高架橋下)",
      "En": "Sec. 1, Minquan E. Rd./Sec. 3, Xinsheng N. Rd"
    },
    "BikesCapacity": 70,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0163",
    "StationID": "0163",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運麟光站",
      "En": "MRT Linguang Sta."
    },
    "StationPosition": {
      "PositionLat": 25.018097,
      "PositionLon": 121.559279
    },
    "StationAddress": {
      "Zh_tw": "和平東路三段/和平東路三段416巷(捷運高架橋下)",
      "En": "Sec. 3, Heping E. Rd./Ln. 416,Sec. 3, Heping E. Rd."
    },
    "BikesCapacity": 72,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0164",
    "StationID": "0164",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運奇岩站",
      "En": "MRT Qiyan Sta."
    },
    "StationPosition": {
      "PositionLat": 25.126286,
      "PositionLon": 121.500801
    },
    "StationAddress": {
      "Zh_tw": "北投路一段/三合街二段(東北側)",
      "En": "Sec. 1, Beitou Rd./Sec. 2, Sanhe St."
    },
    "BikesCapacity": 56,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0165",
    "StationID": "0165",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運唭哩岸站(2號出口)",
      "En": "MRT Qilian Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.120788,
      "PositionLon": 121.505693
    },
    "StationAddress": {
      "Zh_tw": "西安街二段/立農街一段257巷",
      "En": "Sec. 2, Xi'an St./Ln. 257,Sec. 2, Linong St."
    },
    "BikesCapacity": 62,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0166",
    "StationID": "0166",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北市立景美女中",
      "En": "Taipei JingMei Girls High School"
    },
    "StationPosition": {
      "PositionLat": 24.980602,
      "PositionLon": 121.556177
    },
    "StationAddress": {
      "Zh_tw": "木新路三段/一壽街(西北側)",
      "En": "Sec. 3, Muxin Rd./Yishou St."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0167",
    "StationID": "0167",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北市立天文館",
      "En": "Taipei Astronomical Museum"
    },
    "StationPosition": {
      "PositionLat": 25.095714,
      "PositionLon": 121.518046
    },
    "StationAddress": {
      "Zh_tw": "基河路363號前",
      "En": "No.363, Jihe Rd."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0168",
    "StationID": "0168",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "河堤國小",
      "En": "Heti Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.02288,
      "PositionLon": 121.522855
    },
    "StationAddress": {
      "Zh_tw": "金門街12巷23弄1號旁",
      "En": "No.1, Aly. 23, Lane 12, Jinmen St."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0169",
    "StationID": "0169",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "植物園",
      "En": "Taipei Botanical Garden"
    },
    "StationPosition": {
      "PositionLat": 25.030015,
      "PositionLon": 121.509813
    },
    "StationAddress": {
      "Zh_tw": "和平西路二段100號前",
      "En": "No.100, Sec. 2, Heping W. Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0170",
    "StationID": "0170",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新東公園",
      "En": "XinDong Park"
    },
    "StationPosition": {
      "PositionLat": 25.059245,
      "PositionLon": 121.568883
    },
    "StationAddress": {
      "Zh_tw": "民生東路五段/塔悠路(西南側)",
      "En": "Sec. 5, Minsheng E. Rd./Tayou Rd."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0171",
    "StationID": "0171",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "文山運動中心",
      "En": "Taipei Wen Shan Sports Center"
    },
    "StationPosition": {
      "PositionLat": 24.996842,
      "PositionLon": 121.559651
    },
    "StationAddress": {
      "Zh_tw": "興隆路三段/興隆路三段192巷8弄",
      "En": "Sec. 3, Xinglong Rd./Aly. 8, Ln. 192, Sec. 3, Xinglong Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0172",
    "StationID": "0172",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運南京三民站(1號出口)",
      "En": "MRT Nanjing Sanmin Sta. (Exit 1)"
    },
    "StationPosition": {
      "PositionLat": 25.051562,
      "PositionLon": 121.562891
    },
    "StationAddress": {
      "Zh_tw": "南京東路五段/三民路(西北側)",
      "En": "Sec. 5, Nanjing E. Rd./Sanmin Rd."
    },
    "BikesCapacity": 24,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0173",
    "StationID": "0173",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運松江南京站(7號出口)",
      "En": "MRT Songjiang Nanjing Sta. (Exit 7)"
    },
    "StationPosition": {
      "PositionLat": 25.052181,
      "PositionLon": 121.533211
    },
    "StationAddress": {
      "Zh_tw": "松江路/南京東路二段(東北側)",
      "En": "Sec. 2, Nanjing E. Rd./Sec. 2, Nanjing E. Rd."
    },
    "BikesCapacity": 56,
    "SrcUpdateTime": "2018-11-07T09:06:33+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0174",
    "StationID": "0174",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運小巨蛋站(5號出口)",
      "En": "MRT Taipei Arena Sta. (Exit 5)"
    },
    "StationPosition": {
      "PositionLat": 25.051702,
      "PositionLon": 121.553057
    },
    "StationAddress": {
      "Zh_tw": "南京東路四段/健康路(東北側)",
      "En": "Sec. 4, Nanjing E. Rd./Jiankang Rd."
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:49+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0175",
    "StationID": "0175",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運南京復興站(5號出口)",
      "En": "MRT Nanjing Fuxing Sta. (Exit 5)"
    },
    "StationPosition": {
      "PositionLat": 25.051618,
      "PositionLon": 121.544847
    },
    "StationAddress": {
      "Zh_tw": "南京東路三段/南京東路三段256巷(東南側)",
      "En": "Sec. 3, Nanjing E. Rd./Ln. 256, Sec. 3, Nanjing E. Rd."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0176",
    "StationID": "0176",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "興安華城",
      "En": "Xingan Huacheng Community"
    },
    "StationPosition": {
      "PositionLat": 25.055997,
      "PositionLon": 121.542318
    },
    "StationAddress": {
      "Zh_tw": "興安街/遼寧街",
      "En": "Xing’an St./Liaoning St."
    },
    "BikesCapacity": 94,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0177",
    "StationID": "0177",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "葫蘆國小",
      "En": "Hulu Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.082538,
      "PositionLon": 121.507495
    },
    "StationAddress": {
      "Zh_tw": "環河北路三段/葫蘆街(東北側)",
      "En": "Sec. 3, Huanhe N. Rd./Hulu St."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0178",
    "StationID": "0178",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "延平國宅",
      "En": "Yanping Public Housing"
    },
    "StationPosition": {
      "PositionLat": 25.078908,
      "PositionLon": 121.510306
    },
    "StationAddress": {
      "Zh_tw": "延平北路五段一巷40號前",
      "En": "No.40, Ln. 1, Sec. 5, Yanping N. Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0179",
    "StationID": "0179",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南港公園",
      "En": "Nangang Park"
    },
    "StationPosition": {
      "PositionLat": 25.041355,
      "PositionLon": 121.59073
    },
    "StationAddress": {
      "Zh_tw": "福德街383號對面(南港公園出口前)",
      "En": "No.383, Fude St."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0180",
    "StationID": "0180",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "福華商場",
      "En": "Fuhua Market"
    },
    "StationPosition": {
      "PositionLat": 25.06877,
      "PositionLon": 121.592654
    },
    "StationAddress": {
      "Zh_tw": "民權東路六段/民權東路六段180巷(石潭平面停車場內)",
      "En": "Sec. 6, Minquan E. Rd./Ln. 180, Sec. 6, Minquan E. Rd."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0181",
    "StationID": "0181",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "建國和平路口",
      "En": "JianGuo & Heping Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.02585,
      "PositionLon": 121.537383
    },
    "StationAddress": {
      "Zh_tw": "建國南路二段/和平東路二段(西北側)",
      "En": "Sec. 2, Jianguo S. Rd./Sec. 2, Heping E. Rd."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:43+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0182",
    "StationID": "0182",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運古亭站(2號出口)",
      "En": "MRT Guting Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.0253,
      "PositionLon": 121.523537
    },
    "StationAddress": {
      "Zh_tw": "羅斯福路二段/羅斯福路二段174巷(捷運古亭站2號出口前)",
      "En": "Sec. 2, Roosevelt Rd./Ln. 174, Sec. 2, Roosevelt Rd."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0183",
    "StationID": "0183",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "圓環站",
      "En": "Yuanhuan"
    },
    "StationPosition": {
      "PositionLat": 25.05379,
      "PositionLon": 121.514179
    },
    "StationAddress": {
      "Zh_tw": "南京西路/重慶北路一段(西南側)",
      "En": "Nanjing W. Rd./Sec. 1, Chongqing N. Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0184",
    "StationID": "0184",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "劍潭社區",
      "En": "Jiantan Community"
    },
    "StationPosition": {
      "PositionLat": 25.084759,
      "PositionLon": 121.537892
    },
    "StationAddress": {
      "Zh_tw": "通北街143號前",
      "En": "No.143, Tongbei St."
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0185",
    "StationID": "0185",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "瑠公公園",
      "En": "LiuGong Park"
    },
    "StationPosition": {
      "PositionLat": 25.042342,
      "PositionLon": 121.54605
    },
    "StationAddress": {
      "Zh_tw": "大安路一段/大安路一段75巷(西側)",
      "En": "Ln. 75, Sec. 1/Ln. 75, Sec. 1, Da’an Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0186",
    "StationID": "0186",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北市立大學",
      "En": "University of Taipei"
    },
    "StationPosition": {
      "PositionLat": 25.035414,
      "PositionLon": 121.514218
    },
    "StationAddress": {
      "Zh_tw": "愛國西路/公園路(西北側)",
      "En": "Aiguo W. Rd./Gongyuan Rd."
    },
    "BikesCapacity": 82,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0187",
    "StationID": "0187",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "仁愛延吉街口",
      "En": "Renai & Yanji Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.037465,
      "PositionLon": 121.555769
    },
    "StationAddress": {
      "Zh_tw": "仁愛路四段/延吉街(東南側)",
      "En": "Sec. 4, Ren’ai Rd./Yanji St."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:45+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0188",
    "StationID": "0188",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "社子國小",
      "En": "Taipei Municipal Shezi Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.090293,
      "PositionLon": 121.50189
    },
    "StationAddress": {
      "Zh_tw": "延平北路六段/社中街(社子國小對面跨提便道橋下)",
      "En": "Sec. 6, Yanping N. Rd./Shezhong St."
    },
    "BikesCapacity": 56,
    "SrcUpdateTime": "2018-11-07T09:06:20+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0189",
    "StationID": "0189",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "金瑞公園(金龍路)",
      "En": "JinRui Park"
    },
    "StationPosition": {
      "PositionLat": 25.087987,
      "PositionLon": 121.58781
    },
    "StationAddress": {
      "Zh_tw": "金龍路213巷1弄7號前",
      "En": "No.7, Aly. 1, Ln. 213, Jinlong Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0190",
    "StationID": "0190",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運大直站(3號出口)",
      "En": "MRT Dazhi Sta. (Exit 3)"
    },
    "StationPosition": {
      "PositionLat": 25.079278,
      "PositionLon": 121.546683
    },
    "StationAddress": {
      "Zh_tw": "北安路458巷41弄/北安路536巷(捷運大直站3號出口前人行道)",
      "En": "Aly. 41, Ln. 458, Bei’an Rd./Ln. 536, Bei’an Rd."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0191",
    "StationID": "0191",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運大湖公園站(2號出口)",
      "En": "MRT Dahu Park Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.083873,
      "PositionLon": 121.60206
    },
    "StationAddress": {
      "Zh_tw": "成功路五段/大湖山莊街(大湖公園地下停車場旁)",
      "En": "Sec. 5, Chenggong Rd./Dahu Shanzhuang St."
    },
    "BikesCapacity": 58,
    "SrcUpdateTime": "2018-11-07T09:06:45+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0192",
    "StationID": "0192",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運葫洲站(1號出口)",
      "En": "MRT Huzhou Sta. (Exit 1)"
    },
    "StationPosition": {
      "PositionLat": 25.072485,
      "PositionLon": 121.607955
    },
    "StationAddress": {
      "Zh_tw": "康寧路三段/成功路五段450巷21弄(西北側)(捷運葫洲站1號出口前自行車停放區)",
      "En": "Sec. 3, Kangning Rd./Aly. 21, Ln. 450, Sec. 5, Chenggong Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0193",
    "StationID": "0193",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "舊莊區民活動中心",
      "En": "Jiuzhuang Recreation Center"
    },
    "StationPosition": {
      "PositionLat": 25.041277,
      "PositionLon": 121.61935
    },
    "StationAddress": {
      "Zh_tw": "舊莊街一段91巷/舊莊街一段91巷12弄(舊莊區民活動中心前)",
      "En": "Ln. 91, Sec. 1, Jiuzhuang St./Aly. 12, Ln. 91, Sec. 1, Jiuzhuang St."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0194",
    "StationID": "0194",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "市民林森路口",
      "En": "Civic Blvd Linsen Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.047958,
      "PositionLon": 121.524388
    },
    "StationAddress": {
      "Zh_tw": "市民大道二段/林森北路(東北側)",
      "En": "Sec. 2, Civic Blvd./Linsen N. Rd."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0195",
    "StationID": "0195",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "信義杭州路口(中華電信總公司)",
      "En": "Xinyi Hangzhou Intersection(Chunghwa Telecom)"
    },
    "StationPosition": {
      "PositionLat": 25.035851,
      "PositionLon": 121.523987
    },
    "StationAddress": {
      "Zh_tw": "信義路一段/杭州南路一段(西北側)",
      "En": "Sec. 1, Xinyi Rd./Sec. 1, Hangzhou S. Rd."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0196",
    "StationID": "0196",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新湖國小",
      "En": "Xinhu Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.068744,
      "PositionLon": 121.589233
    },
    "StationAddress": {
      "Zh_tw": "民權東路六段/成功路二段320巷31弄(東南側)",
      "En": "Sec. 6, Minquan E. Rd./Aly. 31, Ln. 320, Sec. 2, Chenggong Rd."
    },
    "BikesCapacity": 24,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0197",
    "StationID": "0197",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "饒河夜市(八德路側)",
      "En": "Raohe Night Market"
    },
    "StationPosition": {
      "PositionLat": 25.049845,
      "PositionLon": 121.571885
    },
    "StationAddress": {
      "Zh_tw": "八德路/松信路(西南側)",
      "En": "The S.W. side of St.Wuchang & Road Longjiang."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0201",
    "StationID": "0201",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "東陽公園",
      "En": "Dongyang Park"
    },
    "StationPosition": {
      "PositionLat": 25.057164,
      "PositionLon": 121.597924
    },
    "StationAddress": {
      "Zh_tw": "重陽路125巷26號至36-2號對面人行道",
      "En": "No.26 to No. 36-2, Ln. 125, Chongyang Rd. (opposite)"
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0202",
    "StationID": "0202",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運關渡站",
      "En": "MRT Guandu Sta."
    },
    "StationPosition": {
      "PositionLat": 25.124646,
      "PositionLon": 121.467336
    },
    "StationAddress": {
      "Zh_tw": "大度路三段270巷/立功街55巷(西南側人行道)",
      "En": "Ln. 270, Sec. 3, Dadu Rd./Ln. 55, Ligong St."
    },
    "BikesCapacity": 60,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0203",
    "StationID": "0203",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "古亭國中",
      "En": "Guting Junior High School"
    },
    "StationPosition": {
      "PositionLat": 25.024487,
      "PositionLon": 121.51057
    },
    "StationAddress": {
      "Zh_tw": "中華路二段465號對面人行道(古亭國中)",
      "En": "No.465, Sec. 2, Zhonghua Rd. (opposite)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0204",
    "StationID": "0204",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北市立大學(天母校區)",
      "En": "University of Taipei Tianmu Campus"
    },
    "StationPosition": {
      "PositionLat": 25.113625,
      "PositionLon": 121.53742
    },
    "StationAddress": {
      "Zh_tw": "士東路276號至280號對面人行道",
      "En": "No.276 to No. 280, Shidong Rd., (opposite)"
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0205",
    "StationID": "0205",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "木柵光輝路口",
      "En": "Mucha Guanghui Intersection"
    },
    "StationPosition": {
      "PositionLat": 24.988241,
      "PositionLon": 121.55561
    },
    "StationAddress": {
      "Zh_tw": "木柵路一段290號西側人行道(木柵光輝路口)",
      "En": "No.290, Sec. 1, Muzha Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:43+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0206",
    "StationID": "0206",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運辛亥站",
      "En": "MRT Xinhai Sta."
    },
    "StationPosition": {
      "PositionLat": 25.005386,
      "PositionLon": 121.55716
    },
    "StationAddress": {
      "Zh_tw": "辛亥路四段114號旁人行道(捷運辛亥站)",
      "En": "No.114, Sec. 4, Xinhai Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0207",
    "StationID": "0207",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "福安國中",
      "En": "Fu-an Junior Hight School"
    },
    "StationPosition": {
      "PositionLat": 25.103242,
      "PositionLon": 121.487477
    },
    "StationAddress": {
      "Zh_tw": "延平北路七段250號前人行道(福安國中)",
      "En": "No.250, Sec. 7, Yanping N. Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:20+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0208",
    "StationID": "0208",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "龍山國小",
      "En": "Longshan Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.035555,
      "PositionLon": 121.495342
    },
    "StationAddress": {
      "Zh_tw": "和平西路三段280號對面人行道(龍山國小)",
      "En": "No.280, Sec. 3, Heping W. Rd. (opposite)"
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0209",
    "StationID": "0209",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運復興崗站",
      "En": "MRT Fuxinggang Sta."
    },
    "StationPosition": {
      "PositionLat": 25.137837,
      "PositionLon": 121.486071
    },
    "StationAddress": {
      "Zh_tw": "中央北路三段17-1號對面人行道 (中央北路三段53巷側)",
      "En": "No.17-1, Sec. 3, Zhongyang N. Rd. (opposite)"
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0210",
    "StationID": "0210",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "樂群二敬業四路口",
      "En": "Lequn 2nd & Jingye 4th Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.079766,
      "PositionLon": 121.558135
    },
    "StationAddress": {
      "Zh_tw": "樂群二路180號前廣場",
      "En": "No.180, Lequn 2nd Rd."
    },
    "BikesCapacity": 60,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0211",
    "StationID": "0211",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "星雲金湖街口",
      "En": "Xingyun & Jinhu Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.080915,
      "PositionLon": 121.597339
    },
    "StationAddress": {
      "Zh_tw": "星雲街210巷11號旁平面停車場 ",
      "En": "No.11, Ln. 210, Xingyun St."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:20+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0212",
    "StationID": "0212",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "北安大直街口",
      "En": "Bei'an & Dazhi Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.084223,
      "PositionLon": 121.549452
    },
    "StationAddress": {
      "Zh_tw": "北安路676號前人行道 ",
      "En": "No.676, Bei’an Rd."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0213",
    "StationID": "0213",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "蘭雅國小",
      "En": "Lanya Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.107782,
      "PositionLon": 121.523107
    },
    "StationAddress": {
      "Zh_tw": "磺溪街80號~82號對面人行道(蘭雅國小東側)",
      "En": "No.80 to No.82, Huangxi St. (opposite)"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:36+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0214",
    "StationID": "0214",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "基河一期國宅",
      "En": "Jihe First Phase Republic Housing"
    },
    "StationPosition": {
      "PositionLat": 25.055935,
      "PositionLon": 121.578645
    },
    "StationAddress": {
      "Zh_tw": "南京東路六段131號至137號對面綠地",
      "En": "No.131 to No.137, Sec. 6, Nanjing E. Rd. (opposite)"
    },
    "BikesCapacity": 54,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0215",
    "StationID": "0215",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運北門站(3號出口)",
      "En": "MRT Beimen Sta. (Exit.3)"
    },
    "StationPosition": {
      "PositionLat": 25.04993,
      "PositionLon": 121.510367
    },
    "StationAddress": {
      "Zh_tw": "鄭州路/塔城街(西南側)(捷運北門站3號出口)",
      "En": "Zhengzhou Rd./Tacheng St.(southwest)"
    },
    "BikesCapacity": 62,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0216",
    "StationID": "0216",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "培英公園",
      "En": "Peiying Park"
    },
    "StationPosition": {
      "PositionLat": 25.082553,
      "PositionLon": 121.544601
    },
    "StationAddress": {
      "Zh_tw": "崇實路/大直街62巷(東南側)",
      "En": "Chongshi Rd./Dazhi St. (southeast)"
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0217",
    "StationID": "0217",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北花市",
      "En": "Taipei Flowers Auction"
    },
    "StationPosition": {
      "PositionLat": 25.062645,
      "PositionLon": 121.574267
    },
    "StationAddress": {
      "Zh_tw": "新湖三路28號前人行道",
      "En": "No.28, Xinhu 3rd Rd."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0218",
    "StationID": "0218",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "松山高中",
      "En": "SONG-SHAN Senior High School"
    },
    "StationPosition": {
      "PositionLat": 25.043299,
      "PositionLon": 121.564108
    },
    "StationAddress": {
      "Zh_tw": "基隆路一段172巷15號對面人行道(松山高中)",
      "En": "No.15, Ln. 172, Sec. 1, Keelung Rd. (opposite)"
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:33+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0219",
    "StationID": "0219",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "大理高中",
      "En": "Dali High School"
    },
    "StationPosition": {
      "PositionLat": 25.031147,
      "PositionLon": 121.49074
    },
    "StationAddress": {
      "Zh_tw": "環河南路二段300號對面人行道(大理高中)",
      "En": "No.300, Sec. 2, Huanhe S. Rd. (opposite)"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0220",
    "StationID": "0220",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "大稻埕公園",
      "En": "Dadaocheng Park"
    },
    "StationPosition": {
      "PositionLat": 25.059162,
      "PositionLon": 121.510512
    },
    "StationAddress": {
      "Zh_tw": "安西街1巷15號對面人行道(大稻埕公園)",
      "En": "No.15, Ln. 1, Anxi St. (opposite)"
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0221",
    "StationID": "0221",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "泰和公園",
      "En": "Taihe Park"
    },
    "StationPosition": {
      "PositionLat": 25.019276,
      "PositionLon": 121.57107
    },
    "StationAddress": {
      "Zh_tw": "吳興街583巷67弄(泰和公園)",
      "En": "No.5, Aly. 67, Ln. 600, Wuxing St. (opposite)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:15+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0222",
    "StationID": "0222",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "撫順公園",
      "En": "Fushun Park"
    },
    "StationPosition": {
      "PositionLat": 25.064108,
      "PositionLon": 121.522065
    },
    "StationAddress": {
      "Zh_tw": "中山北路2段180號對面",
      "En": "No.180, Sec. 2, Zhongshan N. Rd. (opposite)"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0223",
    "StationID": "0223",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "清江國小",
      "En": "Qingjiang Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.1274,
      "PositionLon": 121.507267
    },
    "StationAddress": {
      "Zh_tw": "三合街一段/公館路西南側人行道(清江國小)",
      "En": "Sec. 1, Sanhe St./Gongguan Rd."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0224",
    "StationID": "0224",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "社正公園",
      "En": "Shezheng Park"
    },
    "StationPosition": {
      "PositionLat": 25.088243,
      "PositionLon": 121.510535
    },
    "StationAddress": {
      "Zh_tw": "社中街43號對面停車場(社正公園)",
      "En": "No.43, Shezhong St. (opposite)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0225",
    "StationID": "0225",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臥龍樂業街口",
      "En": "Wolong & Leye Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.0186,
      "PositionLon": 121.554839
    },
    "StationAddress": {
      "Zh_tw": "臥龍街267號對面人行道(臥龍樂業街口)",
      "En": "No.267, Wolong St. (opposite)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0226",
    "StationID": "0226",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "向陽南港路口",
      "En": "Xiangyang & Nangang Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.054365,
      "PositionLon": 121.594228
    },
    "StationAddress": {
      "Zh_tw": "向陽路49號旁人行道(向陽南港路口)",
      "En": "No.49, Xiangyang Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0227",
    "StationID": "0227",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "麗山高中",
      "En": "LiShan High School"
    },
    "StationPosition": {
      "PositionLat": 25.084244,
      "PositionLon": 121.57668
    },
    "StationAddress": {
      "Zh_tw": "環山路二段131號對面人行道(麗山高中)",
      "En": "No.131, Sec. 2, Huanshan Rd. (opposite)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0228",
    "StationID": "0228",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運萬芳社區站",
      "En": "MRT Wanfang Community Sta."
    },
    "StationPosition": {
      "PositionLat": 24.998956,
      "PositionLon": 121.567474
    },
    "StationAddress": {
      "Zh_tw": "萬芳路60號西側廣場",
      "En": "No.60, Wanfang Rd. (west side)"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0229",
    "StationID": "0229",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "市民太原路口",
      "En": "Civic & Taiyuan Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.049394,
      "PositionLon": 121.514611
    },
    "StationAddress": {
      "Zh_tw": "鄭州路23號東側人行道(市民太原路口)",
      "En": "No.23, Zhengzhou Rd. (east side)"
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0230",
    "StationID": "0230",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "湖光國宅",
      "En": "Huguang Republic Housing"
    },
    "StationPosition": {
      "PositionLat": 25.075366,
      "PositionLon": 121.580811
    },
    "StationAddress": {
      "Zh_tw": "文德路22巷67號對面綠地",
      "En": "No.67, Ln. 22, Wende Rd. (opposite)"
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0231",
    "StationID": "0231",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "內政部營建署",
      "En": "Construction & Planning Agency"
    },
    "StationPosition": {
      "PositionLat": 25.047805,
      "PositionLon": 121.545022
    },
    "StationAddress": {
      "Zh_tw": "八德路二段342號東側人行道",
      "En": "No.342, Sec. 2, Bade Rd. (east side)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0232",
    "StationID": "0232",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中山天母路口",
      "En": "Zhongshan & Tianmu Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.118843,
      "PositionLon": 121.529738
    },
    "StationAddress": {
      "Zh_tw": "天母西路3-55號前人行道",
      "En": "No.3-55, Tianmu W. Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0233",
    "StationID": "0233",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運忠義站",
      "En": "MRT Zhongyi Sta."
    },
    "StationPosition": {
      "PositionLat": 25.131411,
      "PositionLon": 121.474155
    },
    "StationAddress": {
      "Zh_tw": "中央北路四段262號對面人行道",
      "En": "No.262, Sec. 4, Zhongyang N. Rd. (opposite)"
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0234",
    "StationID": "0234",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "永欣綠地",
      "En": "Yongxin Green Area"
    },
    "StationPosition": {
      "PositionLat": 25.124162,
      "PositionLon": 121.526071
    },
    "StationAddress": {
      "Zh_tw": "行義路1號對面停車場",
      "En": "No.1, Xingyi Rd. (opposite)"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0235",
    "StationID": "0235",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "市民東興路口",
      "En": "Civic Blvd & Dongxing Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.04846,
      "PositionLon": 121.565928
    },
    "StationAddress": {
      "Zh_tw": "市民大道五段193號前方人行道",
      "En": "No.193, Sec. 5, Civic Blvd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0236",
    "StationID": "0236",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "關渡自然公園",
      "En": "Guandu Nature Park"
    },
    "StationPosition": {
      "PositionLat": 25.119292,
      "PositionLon": 121.469138
    },
    "StationAddress": {
      "Zh_tw": "關渡路68號對面人行道",
      "En": "No.68, Guandu Rd. (opposite)"
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:43+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0237",
    "StationID": "0237",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "文山第二行政中心",
      "En": "Wenshan 2nd District Office"
    },
    "StationPosition": {
      "PositionLat": 25.001149,
      "PositionLon": 121.551418
    },
    "StationAddress": {
      "Zh_tw": "興隆路二段130巷30號對面人行道",
      "En": "No.30, Ln. 130, Sec. 2, Xinglong Rd. (opposite)"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0238",
    "StationID": "0238",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "瑞湖陽光街口",
      "En": "Ruihu & Yangguang Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.073119,
      "PositionLon": 121.575965
    },
    "StationAddress": {
      "Zh_tw": "瑞湖街101號對面人行道",
      "En": "No.101, Ruihu St. (opposite)"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0239",
    "StationID": "0239",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新明路321巷口",
      "En": "Ln. 321, Xinming Rd."
    },
    "StationPosition": {
      "PositionLat": 25.056687,
      "PositionLon": 121.584098
    },
    "StationAddress": {
      "Zh_tw": "新明路323號前人行道",
      "En": "No.323, Xinming Rd."
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0240",
    "StationID": "0240",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南京建國路口",
      "En": "Nanjing Jianguo Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.052141,
      "PositionLon": 121.536802
    },
    "StationAddress": {
      "Zh_tw": "南京東路二段/建國北路二段(北側)",
      "En": "Sec. 2, Nanjing E. Rd./Sec. 2, Jianguo N. Rd."
    },
    "BikesCapacity": 58,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0241",
    "StationID": "0241",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "林口公園",
      "En": "Linkou Park"
    },
    "StationPosition": {
      "PositionLat": 25.038943,
      "PositionLon": 121.579146
    },
    "StationAddress": {
      "Zh_tw": "林口街72號對面公園(林口公園)",
      "En": "No.72, Linkou St. (opposite)"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0242",
    "StationID": "0242",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "關渡宮",
      "En": "Kuantu Temple"
    },
    "StationPosition": {
      "PositionLat": 25.117472,
      "PositionLon": 121.463161
    },
    "StationAddress": {
      "Zh_tw": "大度路三段301巷223-5號西北側停車場",
      "En": "No.223-5, Sec. 3, Dadu Rd."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0243",
    "StationID": "0243",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "社子公園",
      "En": "Shezi Park"
    },
    "StationPosition": {
      "PositionLat": 25.090202,
      "PositionLon": 121.506219
    },
    "StationAddress": {
      "Zh_tw": "永平街20巷37弄/永平街20巷11弄(社子公園南側)",
      "En": "Aly. 37, Ln. 20, Yongping St./Aly. 11, Ln. 20, Yongping St."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0244",
    "StationID": "0244",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "復興市民路口",
      "En": "Fuxing & Civic Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.045908,
      "PositionLon": 121.543736
    },
    "StationAddress": {
      "Zh_tw": "復興南路一段36-9號前人行道(復興市民路口)",
      "En": "No.36-9, Sec. 1, Fuxing S. Rd."
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0245",
    "StationID": "0245",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運中山國中站",
      "En": "MRT Zhongshan Junior High School Sta."
    },
    "StationPosition": {
      "PositionLat": 25.060632,
      "PositionLon": 121.544028
    },
    "StationAddress": {
      "Zh_tw": "復興北路370號前方人行道(捷運中山國中站)",
      "En": "No.370, Fuxing N. Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0246",
    "StationID": "0246",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "國立故宮博物院",
      "En": "National Palace Museum"
    },
    "StationPosition": {
      "PositionLat": 25.098743,
      "PositionLon": 121.548086
    },
    "StationAddress": {
      "Zh_tw": "至善路二段155號對面停車場",
      "En": "No.155, Sec. 2, Zhishan Rd.(oppsite)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0247",
    "StationID": "0247",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "木柵公園",
      "En": "Mucha Park"
    },
    "StationPosition": {
      "PositionLat": 24.987144,
      "PositionLon": 121.560627
    },
    "StationAddress": {
      "Zh_tw": "興隆路四段50號前人行道(木柵公園)",
      "En": "No.50, Sec. 4, Xinglong Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0248",
    "StationID": "0248",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "喬治工商",
      "En": "George Cocational High School of Taipei"
    },
    "StationPosition": {
      "PositionLat": 25.027123,
      "PositionLon": 121.555566
    },
    "StationAddress": {
      "Zh_tw": "基隆路二段166號前(喬治工商)",
      "En": "No.166, Sec. 2, Keelung Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0249",
    "StationID": "0249",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中華桂林路口",
      "En": "Zhonghua & Guilin Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.037706,
      "PositionLon": 121.506624
    },
    "StationAddress": {
      "Zh_tw": "中華路一段206號前方廣場",
      "En": "No.206, Sec. 1, Zhonghua Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0250",
    "StationID": "0250",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "忠孝東路三段217巷口",
      "En": "Ln. 217, Sec. 3, Zhongxiao E. Rd"
    },
    "StationPosition": {
      "PositionLat": 25.04184,
      "PositionLon": 121.539873
    },
    "StationAddress": {
      "Zh_tw": "忠孝東路三段221號前方人行道",
      "En": "No.221, Sec. 3, Zhongxiao E. Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:37+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0251",
    "StationID": "0251",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "華齡公園",
      "En": "Hualing Park"
    },
    "StationPosition": {
      "PositionLat": 25.083023,
      "PositionLon": 121.520692
    },
    "StationAddress": {
      "Zh_tw": "劍潭路80對面公園(華齡公園)",
      "En": "No.80, Jiantan Rd.(oppsite)"
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:43+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0252",
    "StationID": "0252",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "大安運動中心",
      "En": "Daan Sports Center"
    },
    "StationPosition": {
      "PositionLat": 25.020544,
      "PositionLon": 121.545608
    },
    "StationAddress": {
      "Zh_tw": "辛亥路三段55號前方人行道(大安運動中心)",
      "En": "No.55, Sec. 3, Xinhai Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0253",
    "StationID": "0253",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "芝山抽水站",
      "En": "Zhishan Pumping Sta."
    },
    "StationPosition": {
      "PositionLat": 25.101423,
      "PositionLon": 121.52799
    },
    "StationAddress": {
      "Zh_tw": "至誠路二段80號對面人行道(芝山抽水站)",
      "En": "No.80, Sec. 2, Zhicheng Rd.(oppsite)"
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0254",
    "StationID": "0254",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "立功立德路口",
      "En": "Ligong Lide Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.125377,
      "PositionLon": 121.471482
    },
    "StationAddress": {
      "Zh_tw": "立功街/立德路(西南側人行道)",
      "En": "Ligong St./Lide Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:04:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0255",
    "StationID": "0255",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "光復南路22巷口",
      "En": "Ln. 22, Guangfu S. Rd."
    },
    "StationPosition": {
      "PositionLat": 25.046914,
      "PositionLon": 121.557674
    },
    "StationAddress": {
      "Zh_tw": "光復南路23號對面人行道",
      "En": "No.23, Guangfu S. Rd.(oppsite)"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0256",
    "StationID": "0256",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中山中正路口",
      "En": "Zhongshan & Zhongzheng  Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.096507,
      "PositionLon": 121.527526
    },
    "StationAddress": {
      "Zh_tw": "中山北路五段609-625號前人行道(中山中正路口)",
      "En": "No.609 to No.625, Sec. 5, Zhongshan N. Rd."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:39+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0257",
    "StationID": "0257",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "錦德公園",
      "En": "Jinde Park"
    },
    "StationPosition": {
      "PositionLat": 25.023316,
      "PositionLon": 121.492637
    },
    "StationAddress": {
      "Zh_tw": "德昌街243號對面公園(錦德公園)",
      "En": "No.243, Dechang St.(oppsite)"
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0258",
    "StationID": "0258",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "聯合醫院中興院區",
      "En": "Taipei City Hospital (Zhongxing Branch)"
    },
    "StationPosition": {
      "PositionLat": 25.052096,
      "PositionLon": 121.507979
    },
    "StationAddress": {
      "Zh_tw": "長安西路299-2號對面人行道",
      "En": "No.299-2, Chang’an W. Rd.(oppsite)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0259",
    "StationID": "0259",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南京遼寧街口",
      "En": "Nanjing & Liaoning Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.051761,
      "PositionLon": 121.542168
    },
    "StationAddress": {
      "Zh_tw": "南京東路三段189號對面(南京遼寧街口東南側)",
      "En": "No.189, Sec. 3, Nanjing E. Rd.(oppsite)"
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0260",
    "StationID": "0260",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民權瑞光路口",
      "En": "Minquan & Ruiguang Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.068616,
      "PositionLon": 121.583991
    },
    "StationAddress": {
      "Zh_tw": "民權東路六段50號前人行道",
      "En": "No.50, Sec. 6, Minquan E. Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0261",
    "StationID": "0261",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "健康新城",
      "En": "Jiankang New Village"
    },
    "StationPosition": {
      "PositionLat": 25.054095,
      "PositionLon": 121.560928
    },
    "StationAddress": {
      "Zh_tw": "健康路177號前人行道(健康新城)",
      "En": "No.177, Jiankang Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0262",
    "StationID": "0262",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "永安藝文館-表演36房",
      "En": "YONG AN ART CENTER - Performing Arts School 36"
    },
    "StationPosition": {
      "PositionLat": 24.984144,
      "PositionLon": 121.569064
    },
    "StationAddress": {
      "Zh_tw": "木新路二段156號前人行道(永安市場)",
      "En": "No.156, Sec. 2, Muxin Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0263",
    "StationID": "0263",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "至善臨溪路口",
      "En": "Zhishan Linxi Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.097103,
      "PositionLon": 121.542153
    },
    "StationAddress": {
      "Zh_tw": "至善路一段/臨溪路(東南側)",
      "En": "Sec. 1, Zhishan Rd./ Linxi Rd. intersection"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0264",
    "StationID": "0264",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "秀山區民活動中心",
      "En": "Xiushan Community Center"
    },
    "StationPosition": {
      "PositionLat": 25.145936,
      "PositionLon": 121.493009
    },
    "StationAddress": {
      "Zh_tw": "秀山路50號北側道路路側",
      "En": "No.50, Xiushan Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0265",
    "StationID": "0265",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中央北路四段30巷口",
      "En": "Ln. 30, Sec. 4, Zhongyang N. Rd."
    },
    "StationPosition": {
      "PositionLat": 25.135394,
      "PositionLon": 121.478
    },
    "StationAddress": {
      "Zh_tw": "中央北路四段30巷8號對面路側",
      "En": "No.8, Ln. 30, Sec. 4, Zhongyang N. Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0266",
    "StationID": "0266",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "洲子一號公園",
      "En": "Zhouzhi Park No.1"
    },
    "StationPosition": {
      "PositionLat": 25.080258,
      "PositionLon": 121.564806
    },
    "StationAddress": {
      "Zh_tw": "基湖路32號南側公園",
      "En": "No.32, Jihu Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0267",
    "StationID": "0267",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "八德中坡路口",
      "En": "Bade & Zhongpo Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.05062,
      "PositionLon": 121.580194
    },
    "StationAddress": {
      "Zh_tw": "八德路四段869號前方人行道",
      "En": "No.869, Sec. 4, Bade Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:20+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0268",
    "StationID": "0268",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南港高工",
      "En": "Nangang Vocational High School"
    },
    "StationPosition": {
      "PositionLat": 25.056655,
      "PositionLon": 121.607055
    },
    "StationAddress": {
      "Zh_tw": "興中路29號前方人行道",
      "En": "No.29, Xingzhong Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0269",
    "StationID": "0269",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "三軍總醫院",
      "En": "Tri-Service General Hospital"
    },
    "StationPosition": {
      "PositionLat": 25.070723,
      "PositionLon": 121.590304
    },
    "StationAddress": {
      "Zh_tw": "成功路二段/成功路二段323巷東北角人行道",
      "En": "Sec. 2, Chenggong Rd./Ln. 323, Sec. 2, Chenggong Rd.(Intersection)"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0270",
    "StationID": "0270",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "雨農國小",
      "En": "Yu Nong Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.105429,
      "PositionLon": 121.529217
    },
    "StationAddress": {
      "Zh_tw": "忠義街6號對面人行道(雨農國小)",
      "En": "No.6, Zhongyi St.(oppsite)"
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0271",
    "StationID": "0271",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "伊通長安路口",
      "En": "Yitong & Chang'an Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.048334,
      "PositionLon": 121.534693
    },
    "StationAddress": {
      "Zh_tw": "伊通街/長安東路二段(交叉口西南側路側)",
      "En": "Yitong St./Sec. 2, Chang’an E. Rd. intersection(Southwest)"
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0272",
    "StationID": "0272",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "忠順區民活動中心",
      "En": "Zhongshun Public Places"
    },
    "StationPosition": {
      "PositionLat": 24.984707,
      "PositionLon": 121.563125
    },
    "StationAddress": {
      "Zh_tw": "忠順街二段22號前方人行道(忠順區民活動中心)",
      "En": "No.22, Sec. 2, Zhongshun St."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0273",
    "StationID": "0273",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "芝山國小",
      "En": "Zhishan Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.110437,
      "PositionLon": 121.535954
    },
    "StationAddress": {
      "Zh_tw": "德行東路/德行東路283巷東北角人行道(芝山國小)",
      "En": "Dexing E. Rd./Ln. 283, Dexing E. Rd.Intersection(northeast)"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:37+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0274",
    "StationID": "0274",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "扶輪親恩公園",
      "En": "Rotary Park"
    },
    "StationPosition": {
      "PositionLat": 25.066997,
      "PositionLon": 121.579833
    },
    "StationAddress": {
      "Zh_tw": "民權東路六段13之15號對面人行道(民權大橋)",
      "En": "No.13-15, Sec. 6, Minquan E. Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0275",
    "StationID": "0275",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "西本願寺廣場",
      "En": "Nishi Honganji Square"
    },
    "StationPosition": {
      "PositionLat": 25.040988,
      "PositionLon": 121.507688
    },
    "StationAddress": {
      "Zh_tw": "中華路一段/長沙街二段路口西南側人行道(西本願寺)",
      "En": "Sec. 1, Zhonghua Rd./Sec. 2, Changsha St. intersection(Southwest)"
    },
    "BikesCapacity": 58,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0276",
    "StationID": "0276",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "三興公園",
      "En": "Sanxing Park"
    },
    "StationPosition": {
      "PositionLat": 25.028679,
      "PositionLon": 121.55932
    },
    "StationAddress": {
      "Zh_tw": "吳興街118巷35弄28號前方(三興公園)",
      "En": "No.28, Aly. 35, Ln. 118, Wuxing St."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0277",
    "StationID": "0277",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中山堂",
      "En": "Zhongshan Hall"
    },
    "StationPosition": {
      "PositionLat": 25.044091,
      "PositionLon": 121.51025
    },
    "StationAddress": {
      "Zh_tw": "延平南路/武昌街一段東南角人行道(延平武昌街口)",
      "En": "Yanping S. Rd./Sec. 1, Wuchang St. intersection(southeast)"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0278",
    "StationID": "0278",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "明美公園",
      "En": "MingMei Park"
    },
    "StationPosition": {
      "PositionLat": 25.062557,
      "PositionLon": 121.586065
    },
    "StationAddress": {
      "Zh_tw": "石潭路/南京東路六段451巷口西南人行道綠帶(明美公園)",
      "En": "Shitan Rd./Ln. 451, Sec. 6, Nanjing E. Rd. intersection(southwest)"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0279",
    "StationID": "0279",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南港車站(興華路)",
      "En": "Nangang Rail Sta.(Xinhua Rd.)"
    },
    "StationPosition": {
      "PositionLat": 25.053432,
      "PositionLon": 121.606331
    },
    "StationAddress": {
      "Zh_tw": "市民大道八段/興華路口西北側人行道",
      "En": "Sec. 8, Civic Blvd./Xinghua Rd. intersection"
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0280",
    "StationID": "0280",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "士林新天地",
      "En": "Shilin New Village"
    },
    "StationPosition": {
      "PositionLat": 25.089034,
      "PositionLon": 121.51732
    },
    "StationAddress": {
      "Zh_tw": "大南路325號前方人行道",
      "En": "No.325, Danan Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0281",
    "StationID": "0281",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "松江公園",
      "En": "Songjiang Park"
    },
    "StationPosition": {
      "PositionLat": 25.050245,
      "PositionLon": 121.532725
    },
    "StationAddress": {
      "Zh_tw": "松江路/松江路84巷(西北側路側)",
      "En": "Songjiang Rd./Ln. 84, Songjiang Rd. intersecton"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:52+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0282",
    "StationID": "0282",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "富台公園",
      "En": "Futai Park"
    },
    "StationPosition": {
      "PositionLat": 25.041935,
      "PositionLon": 121.571999
    },
    "StationAddress": {
      "Zh_tw": "松信路209號前人行道",
      "En": "No.209, Songxin Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:35+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0283",
    "StationID": "0283",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中央北路四段540巷口",
      "En": "Ln. 540, Sec. 4, Zhongyang N. Rd."
    },
    "StationPosition": {
      "PositionLat": 25.127959,
      "PositionLon": 121.4677
    },
    "StationAddress": {
      "Zh_tw": "中央北路四段529號對面",
      "En": "No.529, Sec. 4, Zhongyang N. Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:47+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0284",
    "StationID": "0284",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "華聲公園",
      "En": "Huasheng Park"
    },
    "StationPosition": {
      "PositionLat": 25.096166,
      "PositionLon": 121.522096
    },
    "StationAddress": {
      "Zh_tw": "華聲街17號南側路側(全聯)",
      "En": "No.17, Huasheng St."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0285",
    "StationID": "0285",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "螢橋國小",
      "En": "Ying-Qiao Elementary school"
    },
    "StationPosition": {
      "PositionLat": 25.025966,
      "PositionLon": 121.51377
    },
    "StationAddress": {
      "Zh_tw": "泉州街32號對面人行道(螢橋國小)",
      "En": "No.32, Quanzhou St.(oppsite)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0286",
    "StationID": "0286",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "德明財經科技大學",
      "En": "Takming University of Science and Technology"
    },
    "StationPosition": {
      "PositionLat": 25.086372,
      "PositionLon": 121.565713
    },
    "StationAddress": {
      "Zh_tw": "環山路一段56號對面(德明財經科技大學)",
      "En": "No.56, Sec. 1, Huanshan Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0287",
    "StationID": "0287",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "第二果菜批發市場",
      "En": "Taipei Second Fruits and Vegetables Wholesale Market"
    },
    "StationPosition": {
      "PositionLat": 25.067558,
      "PositionLon": 121.538264
    },
    "StationAddress": {
      "Zh_tw": "民族東路410巷1號對面(第二果菜市場)",
      "En": "No.1, Ln. 410, Minzu E. Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0288",
    "StationID": "0288",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "濟南紹興路口",
      "En": "Jinan & Shaosing Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.041928,
      "PositionLon": 121.524591
    },
    "StationAddress": {
      "Zh_tw": "濟南路一段/紹興南街口東南側",
      "En": "Sec. 1, Jinan Rd / Shaoxing S. St. ( Southeast )"
    },
    "BikesCapacity": 62,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0289",
    "StationID": "0289",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "牯嶺公園",
      "En": "Guling Park"
    },
    "StationPosition": {
      "PositionLat": 25.023377,
      "PositionLon": 121.518835
    },
    "StationAddress": {
      "Zh_tw": "廈門街113巷/牯嶺街口西側",
      "En": "Xiamen St. / Guling St. ( East )"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0290",
    "StationID": "0290",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新生公園",
      "En": "Xinsheng Park"
    },
    "StationPosition": {
      "PositionLat": 25.068387,
      "PositionLon": 121.530188
    },
    "StationAddress": {
      "Zh_tw": "民族東路/吉林路口(西北側)",
      "En": "Minzu E. Rd. / Jilin Rd. ( Northwest )"
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:39+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0291",
    "StationID": "0291",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運松山站(3號出口)",
      "En": "MRT Songshan Sta.(Exit.3)"
    },
    "StationPosition": {
      "PositionLat": 25.049616,
      "PositionLon": 121.577459
    },
    "StationAddress": {
      "Zh_tw": "松山路/市民大道六段(西北側捷運3號出口)",
      "En": "Songshan Rd. / Sec. 6, Civic Blvd. ( Northwest ) MRT Ex.3"
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0292",
    "StationID": "0292",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "合心廣場",
      "En": "Hesin Square"
    },
    "StationPosition": {
      "PositionLat": 25.046361,
      "PositionLon": 121.582848
    },
    "StationAddress": {
      "Zh_tw": "玉成街80號(對面)",
      "En": "No.80, Yucheng St.(oppsite)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0293",
    "StationID": "0293",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "自來水園區",
      "En": "Taipei Water Park"
    },
    "StationPosition": {
      "PositionLat": 25.013284,
      "PositionLon": 121.530037
    },
    "StationAddress": {
      "Zh_tw": "中正區思源街16號對面人行道",
      "En": "No.16, Siyuan St.(oppsite)"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0294",
    "StationID": "0294",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "朱崙商場",
      "En": "Zhulun Market"
    },
    "StationPosition": {
      "PositionLat": 25.047617,
      "PositionLon": 121.540431
    },
    "StationAddress": {
      "Zh_tw": "龍江路15號前方人行道",
      "En": "No.15, Longjiang Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:39+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0295",
    "StationID": "0295",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "敦親公園",
      "En": "Dunqing Park"
    },
    "StationPosition": {
      "PositionLat": 25.023473,
      "PositionLon": 121.541083
    },
    "StationAddress": {
      "Zh_tw": "和平東路二段96巷8之1號(前方)",
      "En": "No.8-1, Ln. 96, Sec. 2, Heping E. Rd."
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0296",
    "StationID": "0296",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "萬和二號公園",
      "En": "Wanhe Park No. 2"
    },
    "StationPosition": {
      "PositionLat": 25.001545,
      "PositionLon": 121.536446
    },
    "StationAddress": {
      "Zh_tw": "萬隆街255號(對面)",
      "En": "No.255, Wanlong St.(oppsite)"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0297",
    "StationID": "0297",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "長沙公園",
      "En": "Changsha Park"
    },
    "StationPosition": {
      "PositionLat": 25.041702,
      "PositionLon": 121.499922
    },
    "StationAddress": {
      "Zh_tw": "環河南路一段280號之1(東側)",
      "En": "No.280-1, Sec. 1, Huanhe S. Rd."
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:37+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0298",
    "StationID": "0298",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "太原五原路口",
      "En": "Taiyuan & Wuyuan Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.056458,
      "PositionLon": 121.516976
    },
    "StationAddress": {
      "Zh_tw": "太原路 / 五原路口(東南側)",
      "En": "Taiyuan Rd. / Wuyuan Rd. Intersection"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0299",
    "StationID": "0299",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "萬華國中",
      "En": "Wanhua Junior High School "
    },
    "StationPosition": {
      "PositionLat": 25.029264,
      "PositionLon": 121.499358
    },
    "StationAddress": {
      "Zh_tw": "西藏路 / 莒光路299巷口(東南側)",
      "En": "Xizang Rd. / Ln. 299, Juguang Rd. Intersection"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0300",
    "StationID": "0300",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "信義基隆路口",
      "En": "Xinyi & Keelung Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.033209,
      "PositionLon": 121.558731
    },
    "StationAddress": {
      "Zh_tw": "信義路四段401號(前方)",
      "En": "No.401, Sec. 4, Xinyi Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0301",
    "StationID": "0301",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "林森長春路口",
      "En": "Linsen & Changchun Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.055062,
      "PositionLon": 121.525383
    },
    "StationAddress": {
      "Zh_tw": "林森北路/長春路口西北角人行道(林森長春路口)",
      "En": "Linsen N. Rd. / Changchun Rd. Intersetion"
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0302",
    "StationID": "0302",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "敦北公園",
      "En": "Dunbei Park"
    },
    "StationPosition": {
      "PositionLat": 25.060746,
      "PositionLon": 121.550711
    },
    "StationAddress": {
      "Zh_tw": "敦化北路 / 富錦街口(東北側)",
      "En": "Dunhua N. Rd. / Fujin St. Intersection"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0303",
    "StationID": "0303",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "安泰街83巷",
      "En": "Ln. 83, Antai St."
    },
    "StationPosition": {
      "PositionLat": 25.076691,
      "PositionLon": 121.617085
    },
    "StationAddress": {
      "Zh_tw": "安泰街83巷3號對面",
      "En": "No.3, Ln. 83, Antai St. ( oppsite )"
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0304",
    "StationID": "0304",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "金華公園",
      "En": "Jinhua Park"
    },
    "StationPosition": {
      "PositionLat": 25.029902,
      "PositionLon": 121.531235
    },
    "StationAddress": {
      "Zh_tw": "金華街251號對面(金華公園)",
      "En": "No.251, Jinhua St."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0305",
    "StationID": "0305",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "碧山公園",
      "En": "Bishan Park"
    },
    "StationPosition": {
      "PositionLat": 25.087413,
      "PositionLon": 121.592253
    },
    "StationAddress": {
      "Zh_tw": "內湖路三段60巷8弄1號(東南側)",
      "En": "No.1, Aly. 8, Ln. 60, Sec. 3, Neihu Rd."
    },
    "BikesCapacity": 46,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0306",
    "StationID": "0306",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運古亭站(6號出口)",
      "En": "MRT Guting Sta.(Exit.6)"
    },
    "StationPosition": {
      "PositionLat": 25.027781,
      "PositionLon": 121.52198
    },
    "StationAddress": {
      "Zh_tw": "羅斯福路二段 / 羅斯福路二段15巷口(西側)",
      "En": "Sec. 2, Roosevelt Rd. / Ln. 15, Sec. 2, Roosevelt Rd."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0307",
    "StationID": "0307",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "仁愛安和路口",
      "En": "Renai & Anhe Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.03757,
      "PositionLon": 121.552076
    },
    "StationAddress": {
      "Zh_tw": "仁愛路四段 / 仁愛路四段222巷(東南側)",
      "En": "Sec. 4, Ren’ai Rd. / Ln. 222, Sec. 4, Ren’ai Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0308",
    "StationID": "0308",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "西松高中",
      "En": "Xisong High School"
    },
    "StationPosition": {
      "PositionLat": 25.055672,
      "PositionLon": 121.567127
    },
    "StationAddress": {
      "Zh_tw": "健康路325巷 / 健康路325巷12弄口(東北側)",
      "En": "Ln. 325, Jiankang Rd. / Aly. 12, Ln. 325, Jiankang Rd. "
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0309",
    "StationID": "0309",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "三軍總醫院(松山分院)",
      "En": "Tri-Service General (Songshan Branch)"
    },
    "StationPosition": {
      "PositionLat": 25.05447,
      "PositionLon": 121.556098
    },
    "StationAddress": {
      "Zh_tw": "光復北路 / 光復北路190巷口(東南側)",
      "En": "Guangfu N. Rd. / Ln. 190, Guangfu N. Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0310",
    "StationID": "0310",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "國立臺北大學(臺北校區)",
      "En": "National Taipei University(Taipei Campus)"
    },
    "StationPosition": {
      "PositionLat": 25.057923,
      "PositionLon": 121.542732
    },
    "StationAddress": {
      "Zh_tw": "民生東路三段 / 復興北路280巷10弄口(西北側)",
      "En": "Sec. 3, Minsheng E. Rd. / Aly. 10, Ln. 280, Fuxing N. Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0311",
    "StationID": "0311",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運忠孝新生站(2號出口)",
      "En": "MRT Zhongxiao Xinsheng Sta.(Exit.2)"
    },
    "StationPosition": {
      "PositionLat": 25.042392,
      "PositionLon": 121.532229
    },
    "StationAddress": {
      "Zh_tw": "忠孝東路二段123號對面(捷運忠孝新生站2號出口)",
      "En": "No.123, Sec. 2, Zhongxiao E. Rd.(oppsite)"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0312",
    "StationID": "0312",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運信義安和站(1號出口)",
      "En": "MRT Xinyi Anhe Sta.(Exit.1)"
    },
    "StationPosition": {
      "PositionLat": 25.033323,
      "PositionLon": 121.552787
    },
    "StationAddress": {
      "Zh_tw": "信義路四段 / 安和路一段口(東北側)",
      "En": "Sec. 4, Xinyi Rd. / Sec. 1, Anhe Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0313",
    "StationID": "0313",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "光華商場",
      "En": "Guang Hua Computer Market"
    },
    "StationPosition": {
      "PositionLat": 25.04515,
      "PositionLon": 121.532738
    },
    "StationAddress": {
      "Zh_tw": "市民大道三段/新生北路一段路口西南側人行道(光華商場)",
      "En": "Sec. 3, Civic Blvd. / Sec. 1, Xinsheng N. Rd. intersection"
    },
    "BikesCapacity": 64,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0314",
    "StationID": "0314",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "敦化長春路口",
      "En": "Dunhua & Changchun Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.053614,
      "PositionLon": 121.54872
    },
    "StationAddress": {
      "Zh_tw": "敦化北路 / 敦化北路120巷口(西南側)",
      "En": "Dunhua N. Rd. / Ln. 120, Dunhua N. Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0315",
    "StationID": "0315",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運萬隆站(1號出口)",
      "En": "MRT Wanlong Sta.(Exit.1)"
    },
    "StationPosition": {
      "PositionLat": 25.001447,
      "PositionLon": 121.539037
    },
    "StationAddress": {
      "Zh_tw": "羅斯福路五段 / 羅斯福路五段236巷口(南側)",
      "En": "Sec. 5, Roosevelt Rd. / Ln. 236, Sec. 5, Roosevelt Rd. intersection"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0316",
    "StationID": "0316",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民有一號公園",
      "En": "Minyou first Park"
    },
    "StationPosition": {
      "PositionLat": 25.060911,
      "PositionLon": 121.54763
    },
    "StationAddress": {
      "Zh_tw": "敦化北路244巷 / 民權東路三段160巷口(西南側)",
      "En": "Ln. 244, Dunhua N. Rd. / Ln. 160, Sec. 3, Minquan E. Rd. intersection"
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:15+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0317",
    "StationID": "0317",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "雙園國中",
      "En": "Shuangyuan Junior High School"
    },
    "StationPosition": {
      "PositionLat": 25.026823,
      "PositionLon": 121.491675
    },
    "StationAddress": {
      "Zh_tw": "西園路二段320巷 / 興義街(西北側)",
      "En": "Ln. 320, Sec. 2, Xiyuan Rd. / Xingyi St. intersection"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:20+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0318",
    "StationID": "0318",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "成功金龍路口",
      "En": "Chenggong & Jinlong Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.084135,
      "PositionLon": 121.59484
    },
    "StationAddress": {
      "Zh_tw": "成功路四段/金龍路口(捷運內湖站1號出口)",
      "En": "Sec. 4, Chenggong Rd. / Jinlong Rd. intersection"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0319",
    "StationID": "0319",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民族林森路口",
      "En": "Minzu & Linsen Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.068507,
      "PositionLon": 121.525322
    },
    "StationAddress": {
      "Zh_tw": "民族東路 / 林森北路口(西北側)",
      "En": "Minzu E. Rd. / Linsen N. Rd. intersection"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0320",
    "StationID": "0320",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運南京三民站(3號出口)",
      "En": "MRT Nanjing Sanmin Sta.(Exit.3)"
    },
    "StationPosition": {
      "PositionLat": 25.051287,
      "PositionLon": 121.564262
    },
    "StationAddress": {
      "Zh_tw": "南京東路五段204號(前方)",
      "En": "No.204, Sec. 5, Nanjing E. Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0321",
    "StationID": "0321",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "莒光大埔街口",
      "En": "Juguang & Dapu Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.031334,
      "PositionLon": 121.505085
    },
    "StationAddress": {
      "Zh_tw": "莒光路/大埔街口東北側(莒光大埔街口)",
      "En": "Juguang Rd. / Dapu St. intersetion"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:15+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0322",
    "StationID": "0322",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "永盛公園(民生東路一段23巷)",
      "En": "Yongsheng Park"
    },
    "StationPosition": {
      "PositionLat": 25.058835,
      "PositionLon": 121.52504
    },
    "StationAddress": {
      "Zh_tw": "民生東路一段23巷 / 民生東路一段27巷口(北側)",
      "En": ""
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:36+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0323",
    "StationID": "0323",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新興公園",
      "En": "Xinxing Park"
    },
    "StationPosition": {
      "PositionLat": 25.061568,
      "PositionLon": 121.524392
    },
    "StationAddress": {
      "Zh_tw": "錦州街13巷 / 中山北路二段137巷口(東南側)",
      "En": "Ln. 13, Jinzhou St. / Ln. 137, Sec. 2, Zhongshan N. Rd."
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0324",
    "StationID": "0324",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "市立圖書館葫蘆堵分館",
      "En": "Taipei Public Library Huludu Branch"
    },
    "StationPosition": {
      "PositionLat": 25.08221,
      "PositionLon": 121.5108
    },
    "StationAddress": {
      "Zh_tw": "延平北路5段136巷4號對面",
      "En": "No.4, Ln. 136, Sec. 5, Zhongshan N. Rd.(oppsite)"
    },
    "BikesCapacity": 24,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0325",
    "StationID": "0325",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南京東路六段368巷",
      "En": "Ln. 368, Sec. 6, Nanjing E. Rd."
    },
    "StationPosition": {
      "PositionLat": 25.05827,
      "PositionLon": 121.58707
    },
    "StationAddress": {
      "Zh_tw": "南京東路六段368巷30號對面人行道",
      "En": "No.30, Ln. 368, Sec. 6, Nanjing E. Rd."
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0326",
    "StationID": "0326",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "基隆路一段101巷口",
      "En": "Ln. 101,Sec. 1,Keelung Rd."
    },
    "StationPosition": {
      "PositionLat": 25.04525,
      "PositionLon": 121.56709
    },
    "StationAddress": {
      "Zh_tw": "基隆路一段 / 基隆路一段101巷口(東南側)",
      "En": "Sec. 1, Keelung Rd. /  Ln. 101, Sec. 1, Keelung Rd. (intersection)"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:43+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0327",
    "StationID": "0327",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "重慶南海路口",
      "En": "Chongqing & Nanhai Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.03158,
      "PositionLon": 121.51464
    },
    "StationAddress": {
      "Zh_tw": "重慶南路二段45號前方(郵政博物館前)",
      "En": "No.45, Sec. 2, Chongqing S. Rd."
    },
    "BikesCapacity": 24,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0328",
    "StationID": "0328",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "一江公園",
      "En": "Yijiang Park"
    },
    "StationPosition": {
      "PositionLat": 25.05316,
      "PositionLon": 121.53146
    },
    "StationAddress": {
      "Zh_tw": "一江街 / 松江路132巷口(西北側)",
      "En": "Yijiang St. /  Ln. 132, Songjiang Rd. intersection"
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0329",
    "StationID": "0329",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "樂群二明水路口",
      "En": "Lequn 2nd & Mingshui Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.07983,
      "PositionLon": 121.55236
    },
    "StationAddress": {
      "Zh_tw": "樂群二路 / 明水路口(東側)",
      "En": "Lequn 2nd Rd. / Mingshui Rd. intersetion"
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0330",
    "StationID": "0330",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "迪化休閒運動公園",
      "En": "Dihua Park"
    },
    "StationPosition": {
      "PositionLat": 25.07491,
      "PositionLon": 121.5115
    },
    "StationAddress": {
      "Zh_tw": "延平北路四段200號(南側)",
      "En": "No.200, Sec. 4, Yanping N. Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0331",
    "StationID": "0331",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民族玉門街口",
      "En": "Minzu & Yumen Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.06859,
      "PositionLon": 121.51974
    },
    "StationAddress": {
      "Zh_tw": "民族西路 / 民族西路31巷口(東北側)",
      "En": "Minsheng W. Rd. / Ln. 31, Minsheng W. Rd. intersection"
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0332",
    "StationID": "0332",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運中山站(2號出口)",
      "En": "MRT Zhongshan Sta. (Exit 2)"
    },
    "StationPosition": {
      "PositionLat": 25.05225,
      "PositionLon": 121.52193
    },
    "StationAddress": {
      "Zh_tw": "南京西路6號(前方)",
      "En": "No.6, Nanjing W. Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0333",
    "StationID": "0333",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "復盛公園",
      "En": "Fusheng Park"
    },
    "StationPosition": {
      "PositionLat": 25.047428,
      "PositionLon": 121.561182
    },
    "StationAddress": {
      "Zh_tw": "八德路四段106巷6弄2號(東側)",
      "En": "No.2, Aly. 6, Ln. 106, Sec. 4, Bade Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:46+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0334",
    "StationID": "0334",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "敦化南路二段103巷口",
      "En": "Ln. 103,Sec. 2,Dunhua S. Rd."
    },
    "StationPosition": {
      "PositionLat": 25.028973,
      "PositionLon": 121.549024
    },
    "StationAddress": {
      "Zh_tw": "敦化南路二段97-101號(西側)",
      "En": "No.97, Sec. 2, Dunhua S. Rd."
    },
    "BikesCapacity": 24,
    "SrcUpdateTime": "2018-11-07T09:06:43+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0335",
    "StationID": "0335",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "景文中學",
      "En": "Jingwen High School"
    },
    "StationPosition": {
      "PositionLat": 24.986301,
      "PositionLon": 121.567855
    },
    "StationAddress": {
      "Zh_tw": "保儀路/木柵路三段102巷口(西南側)",
      "En": "Baoyi Rd. / Ln. 102, Sec. 3, Muzha Rd. ( Intersection )"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:24+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0336",
    "StationID": "0336",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "承德路三段8巷口",
      "En": "Ln. 8,Sec. 3,Chengde Rd."
    },
    "StationPosition": {
      "PositionLat": 25.06382,
      "PositionLon": 121.51815
    },
    "StationAddress": {
      "Zh_tw": "承德路三段12號(前方)",
      "En": "No.12, Sec. 3, Chengde Rd."
    },
    "BikesCapacity": 22,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0337",
    "StationID": "0337",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "彩虹橋",
      "En": "Rainbow Bridge"
    },
    "StationPosition": {
      "PositionLat": 25.05301,
      "PositionLon": 121.57592
    },
    "StationAddress": {
      "Zh_tw": "潭美街27號西側(行善公園東南角)",
      "En": "No.27, Tanmei St."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0338",
    "StationID": "0338",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "成德國中",
      "En": "Chengde Junior High School"
    },
    "StationPosition": {
      "PositionLat": 25.04573,
      "PositionLon": 121.58794
    },
    "StationAddress": {
      "Zh_tw": "東新街108巷10之1號(西側)",
      "En": "No.10-1, Ln. 108, Dongxin St."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0339",
    "StationID": "0339",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "重慶國中",
      "En": "Chongcing Junior High School"
    },
    "StationPosition": {
      "PositionLat": 25.07581,
      "PositionLon": 121.51816
    },
    "StationAddress": {
      "Zh_tw": "敦煌路68號(北側)",
      "En": "No.68, Dunhuang Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:45+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0340",
    "StationID": "0340",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南京光復路口",
      "En": "Nanjing Guangfu Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.05143,
      "PositionLon": 121.55716
    },
    "StationAddress": {
      "Zh_tw": "南京東路四段182號(北側)",
      "En": "No.182, Sec. 4, Nanjing E. Rd."
    },
    "BikesCapacity": 22,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0341",
    "StationID": "0341",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運芝山站(1號出口)",
      "En": "MRT Zhishan Sta.(Exit.1)"
    },
    "StationPosition": {
      "PositionLat": 25.10094,
      "PositionLon": 121.52243
    },
    "StationAddress": {
      "Zh_tw": "文林路 / 福華路口(東側)",
      "En": "Wenlin Rd. / Fuhua Rd. Intersection"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0342",
    "StationID": "0342",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "文林建民路口",
      "En": "Wenlin & Jianmin Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.10779,
      "PositionLon": 121.51468
    },
    "StationAddress": {
      "Zh_tw": "文林北路224-238號(東南側)",
      "En": "No.224 - 238, Wenlin N. Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:36+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0343",
    "StationID": "0343",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "忠孝東路六段185巷口",
      "En": "Ln. 185, Sec. 6, Zhongxiao E. Rd"
    },
    "StationPosition": {
      "PositionLat": 25.04904,
      "PositionLon": 121.58755
    },
    "StationAddress": {
      "Zh_tw": "忠孝東路六段187號(東南側)",
      "En": "No.187, Sec. 6, Zhongxiao E. Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0344",
    "StationID": "0344",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運忠孝復興站(5號出口)",
      "En": "MRT Zhongxiao Fuxing Sta.(Exit.5)"
    },
    "StationPosition": {
      "PositionLat": 25.04264,
      "PositionLon": 121.54401
    },
    "StationAddress": {
      "Zh_tw": "復興南路一段133號(西南側)",
      "En": "No.133, Sec. 1, Fuxing S. Rd."
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0345",
    "StationID": "0345",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中正運動中心",
      "En": "Zhongzheng Sports Center"
    },
    "StationPosition": {
      "PositionLat": 25.03806,
      "PositionLon": 121.51943
    },
    "StationAddress": {
      "Zh_tw": "信義路一段1號(西側)",
      "En": "No.1, Sec. 1, Xinyi Rd."
    },
    "BikesCapacity": 52,
    "SrcUpdateTime": "2018-11-07T09:06:42+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0346",
    "StationID": "0346",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "陽明高中",
      "En": "Yangming High School"
    },
    "StationPosition": {
      "PositionLat": 25.09157,
      "PositionLon": 121.51669
    },
    "StationAddress": {
      "Zh_tw": "中正路510號(西南側)",
      "En": "No.510, Zhongzheng Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:37+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0347",
    "StationID": "0347",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "博愛寶慶路口",
      "En": "Boai & Baoqing Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.04134,
      "PositionLon": 121.51135
    },
    "StationAddress": {
      "Zh_tw": "博愛路 / 寶慶路口(西北側)",
      "En": "Bo’ai Rd. / Baoqing Rd. intersection"
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:49+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0348",
    "StationID": "0348",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民生立體停車場",
      "En": "Minsheng Parking Lot"
    },
    "StationPosition": {
      "PositionLat": 25.05794,
      "PositionLon": 121.55945
    },
    "StationAddress": {
      "Zh_tw": "民生東路五段82號(東側)",
      "En": "No.82, Sec. 5, Minsheng E. Rd."
    },
    "BikesCapacity": 24,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0349",
    "StationID": "0349",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "重慶酒泉街口",
      "En": "Chongqing & Jiuquan Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.07183,
      "PositionLon": 121.51364
    },
    "StationAddress": {
      "Zh_tw": "重慶北路三段272號(東側)",
      "En": "No.272, Sec. 3, Chongqing N. Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0350",
    "StationID": "0350",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "復興南路二段128巷口",
      "En": "Ln. 128, Sec. 2, Fuxing S. Rd."
    },
    "StationPosition": {
      "PositionLat": 25.02904,
      "PositionLon": 121.54336
    },
    "StationAddress": {
      "Zh_tw": "復興南路二段144-3號前方",
      "En": "No.144-3, Sec. 2, Fuxing S. Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0351",
    "StationID": "0351",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中山青島路口",
      "En": "Zhongshan & Qingdao Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.04469,
      "PositionLon": 121.51954
    },
    "StationAddress": {
      "Zh_tw": "中山南路 / 青島東路口東北側",
      "En": "Zhongshan S. Rd. / Qingdao E. Rd. intersection"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0352",
    "StationID": "0352",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民權迪化街口",
      "En": "Minquan & Dihua Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.06318,
      "PositionLon": 121.50944
    },
    "StationAddress": {
      "Zh_tw": "迪化街一段351號(東北側)",
      "En": "No.351, Sec. 1, Dihua St."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0353",
    "StationID": "0353",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "紀州庵",
      "En": "Kishu An Forest of Literature"
    },
    "StationPosition": {
      "PositionLat": 25.02088,
      "PositionLon": 121.52049
    },
    "StationAddress": {
      "Zh_tw": "水源路 / 同安街口 (東側)",
      "En": "No.107, Tong’an St."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:37+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0354",
    "StationID": "0354",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "建國濟南路口",
      "En": "Jianguo & Jinan Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.040033,
      "PositionLon": 121.538084
    },
    "StationAddress": {
      "Zh_tw": "建國南路一段/濟南路三段口(東南側)",
      "En": "Sec. 1, Jianguo S. Rd. / Sec. 3, Jinan Rd. intersection"
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:27+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0355",
    "StationID": "0355",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "福山公園",
      "En": "Fushan Park"
    },
    "StationPosition": {
      "PositionLat": 25.04478,
      "PositionLon": 121.61759
    },
    "StationAddress": {
      "Zh_tw": "研究院路二段61巷15號(東側)",
      "En": "No.15, Ln. 61, Sec. 2, Academia Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0356",
    "StationID": "0356",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺北市網球中心",
      "En": "Taipei Tennis Center"
    },
    "StationPosition": {
      "PositionLat": 25.0674,
      "PositionLon": 121.59749
    },
    "StationAddress": {
      "Zh_tw": "民權東路六段/民權東路六段210巷口(西南側)",
      "En": "Sec. 6, Minquan E. Rd. / Ln. 210, Sec. 6, Minquan E. Rd. intersection"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0357",
    "StationID": "0357",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "松友公園",
      "En": "@Songyou Park"
    },
    "StationPosition": {
      "PositionLat": 25.03423,
      "PositionLon": 121.57636
    },
    "StationAddress": {
      "Zh_tw": "信義路六段76巷2弄16號(南側)",
      "En": "No.16, Aly. 2, Ln. 76, Sec. 6, Xinyi Rd."
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:18+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0358",
    "StationID": "0358",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新明成功路口",
      "En": "Xinming & Chenggong Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.06058,
      "PositionLon": 121.5911
    },
    "StationAddress": {
      "Zh_tw": "新明路/成功路二段口(西南側)",
      "En": "Xinming Rd. / Sec. 2, Chenggong Rd. intersection"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:57+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0359",
    "StationID": "0359",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "健安新城",
      "En": "Jianan Sincheng"
    },
    "StationPosition": {
      "PositionLat": 25.05601,
      "PositionLon": 121.56358
    },
    "StationAddress": {
      "Zh_tw": "三民路41號(東側)",
      "En": "No.41, Sanmin Rd. "
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0360",
    "StationID": "0360",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民權建國路口",
      "En": "Minquan & Jianguo Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.06252,
      "PositionLon": 121.53754
    },
    "StationAddress": {
      "Zh_tw": "民權東路三段/建國北路三段口(東北側)",
      "En": "Sec. 3, Minquan E. Rd. / Sec. 3, Jianguo N. Rd. intersection"
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0361",
    "StationID": "0361",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "振興醫院",
      "En": "Cheng Hsin General Hospital"
    },
    "StationPosition": {
      "PositionLat": 25.1177,
      "PositionLon": 121.5222
    },
    "StationAddress": {
      "Zh_tw": "振興街/明德路口(西北側)",
      "En": "No.41, Zhenxing St. / No.41, Mingde Rd. intersection"
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0362",
    "StationID": "0362",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "和平金山路口",
      "En": "Heping & Jinshan Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.02672,
      "PositionLon": 121.52533
    },
    "StationAddress": {
      "Zh_tw": "和平東路一段 / 金山南路二段口(西南側)",
      "En": "Sec. 1, Heping E. Rd. / Sec. 2, Jinshan S. Rd. intersection"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0363",
    "StationID": "0363",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "復興南路一段340巷口",
      "En": "Ln. 340, Sec. 1, Fuxing S. Rd."
    },
    "StationPosition": {
      "PositionLat": 25.03617,
      "PositionLon": 121.5435
    },
    "StationAddress": {
      "Zh_tw": "復興南路一段322號(東南側)",
      "En": "No.322, Sec. 1, Fuxing S. Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:41+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0364",
    "StationID": "0364",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "嘉興公園",
      "En": "Jiaxing Park"
    },
    "StationPosition": {
      "PositionLat": 25.02109,
      "PositionLon": 121.55219
    },
    "StationAddress": {
      "Zh_tw": "樂業街101巷 / 樂業街口(北側側)",
      "En": "Ln. 101, Leye St. / Leye St. intersection"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0365",
    "StationID": "0365",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "陽明大學",
      "En": "National Yang-Ming University"
    },
    "StationPosition": {
      "PositionLat": 25.11912,
      "PositionLon": 121.51223
    },
    "StationAddress": {
      "Zh_tw": "東華街二段136號(南側)",
      "En": "No.136, Sec. 2, Donghua St."
    },
    "BikesCapacity": 50,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0366",
    "StationID": "0366",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "碧湖公園",
      "En": "Bihu Park"
    },
    "StationPosition": {
      "PositionLat": 25.07988,
      "PositionLon": 121.58287
    },
    "StationAddress": {
      "Zh_tw": "內湖路二段/內湖路二段103巷口(東北側)",
      "En": "Sec. 2, Neihu Rd. / Ln. 103, Sec. 2, Neihu Rd. intersection"
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0367",
    "StationID": "0367",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "豐年公園",
      "En": "Fengnian Park"
    },
    "StationPosition": {
      "PositionLat": 25.13597,
      "PositionLon": 121.497019
    },
    "StationAddress": {
      "Zh_tw": "大業路539號(東側)",
      "En": "No.539, Daye Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:30+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0368",
    "StationID": "0368",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "臺灣戲曲中心",
      "En": "The Xiqu Center of Taiwan"
    },
    "StationPosition": {
      "PositionLat": 25.10208,
      "PositionLon": 121.51979
    },
    "StationAddress": {
      "Zh_tw": "文林路751號(南側)",
      "En": "No.751, Wenlin Rd."
    },
    "BikesCapacity": 44,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0369",
    "StationID": "0369",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "世新大學",
      "En": "Shih Hsin University"
    },
    "StationPosition": {
      "PositionLat": 24.98862,
      "PositionLon": 121.54361
    },
    "StationAddress": {
      "Zh_tw": "木柵路一段17巷1號(西側)",
      "En": "No.1, Ln. 17, Sec. 1, Muzha Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0370",
    "StationID": "0370",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新和國小",
      "En": "Xinhe Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.02656,
      "PositionLon": 121.50242
    },
    "StationAddress": {
      "Zh_tw": "中華路二段416巷/萬大路277巷37弄口(東側)",
      "En": "Ln. 416, Sec. 2, Zhonghua Rd. / Aly. 37, Ln. 277, Wanda Rd. intersection"
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:34+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0371",
    "StationID": "0371",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南門國中",
      "En": "Nanmen Junior High School"
    },
    "StationPosition": {
      "PositionLat": 25.03532,
      "PositionLon": 121.50834
    },
    "StationAddress": {
      "Zh_tw": "廣州街8巷/廣州街口(東南側)",
      "En": "Ln. 8, Guangzhou St. / Guangzhou St. intersection"
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:17+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0372",
    "StationID": "0372",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "重慶民族路口",
      "En": "Chongqing & Minzu Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.06825,
      "PositionLon": 121.51359
    },
    "StationAddress": {
      "Zh_tw": "重慶北路三段154號(前方/東側)",
      "En": "No.154, Sec. 3, Chongqing N. Rd."
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:33+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0373",
    "StationID": "0373",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "中崙福成宮",
      "En": "Zhonglun Fucheng Temple"
    },
    "StationPosition": {
      "PositionLat": 25.04525,
      "PositionLon": 121.546635
    },
    "StationAddress": {
      "Zh_tw": "市民大道四段63號",
      "En": "No.63, Sec. 4, Civic Blvd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0374",
    "StationID": "0374",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "麗湖國小",
      "En": "Lihu Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.073322,
      "PositionLon": 121.602225
    },
    "StationAddress": {
      "Zh_tw": "金湖路363巷5號對側",
      "En": "No.5, Ln. 363, Jinhu Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0375",
    "StationID": "0375",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "銘傳大學",
      "En": "Ming Chuan University"
    },
    "StationPosition": {
      "PositionLat": 25.087714,
      "PositionLon": 121.526766
    },
    "StationAddress": {
      "Zh_tw": "中山北路五段250號(銘傳大學對側)",
      "En": "No.250, Sec. 5, Zhongshan N. Rd."
    },
    "BikesCapacity": 48,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0376",
    "StationID": "0376",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民生建國路口",
      "En": "Minsheng & Jianguo Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.057778,
      "PositionLon": 121.536915
    },
    "StationAddress": {
      "Zh_tw": "民生東路三段 / 建國北路二段口",
      "En": "Sec. 3, Minsheng E. Rd. / Sec. 2, Jianguo N. Rd."
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0377",
    "StationID": "0377",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南港路二段178巷口",
      "En": "Ln. 178, Sec. 2, Nangang Rd."
    },
    "StationPosition": {
      "PositionLat": 25.053675,
      "PositionLon": 121.599693
    },
    "StationAddress": {
      "Zh_tw": "南港路二段 / 南港路二段178巷口(北側)",
      "En": "No.146, Sec. 2, Nangang Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0378",
    "StationID": "0378",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "陽光街321巷口",
      "En": "Ln. 321, Yangguang St."
    },
    "StationPosition": {
      "PositionLat": 25.073193,
      "PositionLon": 121.578691
    },
    "StationAddress": {
      "Zh_tw": "陽光街321巷 / 陽光街口(南側)",
      "En": "Ln. 321, Yangguang St. / Yangguang St."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:32+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0379",
    "StationID": "0379",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "春光公園",
      "En": "Chunguang Park"
    },
    "StationPosition": {
      "PositionLat": 25.042619,
      "PositionLon": 121.580762
    },
    "StationAddress": {
      "Zh_tw": "忠孝東路五段721號(對側)",
      "En": "No.721, Sec. 5, Zhongxiao E. Rd."
    },
    "BikesCapacity": 38,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0380",
    "StationID": "0380",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "塔悠疏散門",
      "En": "Tayou Evacuation Gate"
    },
    "StationPosition": {
      "PositionLat": 25.064713,
      "PositionLon": 121.567899
    },
    "StationAddress": {
      "Zh_tw": "塔悠路 / 撫遠街389巷口(南側)",
      "En": "Tayou Rd. / Ln. 389, Fuyuan St."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:38+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0381",
    "StationID": "0381",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民權東路六段15巷",
      "En": "Ln. 15, Sec. 6, Minquan E. Rd."
    },
    "StationPosition": {
      "PositionLat": 25.06853,
      "PositionLon": 121.578125
    },
    "StationAddress": {
      "Zh_tw": "民權東路六段15巷35號",
      "En": "No.35, Ln. 15, Sec. 6, Minquan E. Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0382",
    "StationID": "0382",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "聯合醫院和平院區",
      "En": "City Hospital (Heping Branch)"
    },
    "StationPosition": {
      "PositionLat": 25.03516,
      "PositionLon": 121.50639
    },
    "StationAddress": {
      "Zh_tw": "中華路二段33號(南側)",
      "En": "No.33, Sec. 2, Zhonghua Rd."
    },
    "BikesCapacity": 42,
    "SrcUpdateTime": "2018-11-07T09:01:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0383",
    "StationID": "0383",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "一壽橋",
      "En": "Yishou Bridge"
    },
    "StationPosition": {
      "PositionLat": 24.97848,
      "PositionLon": 121.55545
    },
    "StationAddress": {
      "Zh_tw": "樟新街64號前方",
      "En": "No.64, Zhangxin St."
    },
    "BikesCapacity": 26,
    "SrcUpdateTime": "2018-11-07T09:06:43+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0384",
    "StationID": "0384",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "松基公園",
      "En": "Songji Park"
    },
    "StationPosition": {
      "PositionLat": 25.05491,
      "PositionLon": 121.5448
    },
    "StationAddress": {
      "Zh_tw": "長春路339巷 / 復興北路189巷口",
      "En": "Ln. 339, Changchun Rd. / Ln. 189, Fuxing N. Rd. intersection"
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0385",
    "StationID": "0385",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "和興路26巷口",
      "En": "Ln.26 ,Hexing Rd."
    },
    "StationPosition": {
      "PositionLat": 24.9856,
      "PositionLon": 121.54531
    },
    "StationAddress": {
      "Zh_tw": "和興路44巷 / 和興路26巷口",
      "En": "Ln. 44, Hexing Rd. / Ln. 26, Hexing Rd. intersection"
    },
    "BikesCapacity": 40,
    "SrcUpdateTime": "2018-11-07T09:06:21+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0386",
    "StationID": "0386",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "錦州吉林路口",
      "En": "Jinzhou & Jilin Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.06029,
      "PositionLon": 121.52981
    },
    "StationAddress": {
      "Zh_tw": "錦州街162號前方",
      "En": "No.162, Jinzhou St."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:19+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0387",
    "StationID": "0387",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "吳興街260巷",
      "En": "Ln. 260,Wuxing St."
    },
    "StationPosition": {
      "PositionLat": 25.0261,
      "PositionLon": 121.56316
    },
    "StationAddress": {
      "Zh_tw": "吳興街260巷 / 吳興街260巷19弄口",
      "En": "Ln. 260, Wuxing St. / Aly. 19, Ln. 260, Wuxing St."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:29+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0388",
    "StationID": "0388",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "景華街128巷口",
      "En": "Ln.128,Jinghua St."
    },
    "StationPosition": {
      "PositionLat": 24.995563,
      "PositionLon": 121.547092
    },
    "StationAddress": {
      "Zh_tw": "景華街126號前方",
      "En": "No.126, Jinghua St."
    },
    "BikesCapacity": 24,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0389",
    "StationID": "0389",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "福德國小",
      "En": "Fude Elementary School"
    },
    "StationPosition": {
      "PositionLat": 25.038324,
      "PositionLon": 121.586245
    },
    "StationAddress": {
      "Zh_tw": "福德街251巷2號(對面/東側)",
      "En": "No.2, Ln. 251, Fude St."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:43+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0390",
    "StationID": "0390",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "稻香重三路口",
      "En": "Daoxiang & Chongsan Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.139937,
      "PositionLon": 121.489594
    },
    "StationAddress": {
      "Zh_tw": "稻香路 / 稻香路43巷口(西北側)",
      "En": "Daoxiang Rd. / Ln. 43, Daoxiang Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0391",
    "StationID": "0391",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "景仁公園",
      "En": "Jingren Park"
    },
    "StationPosition": {
      "PositionLat": 24.9966,
      "PositionLon": 121.540295
    },
    "StationAddress": {
      "Zh_tw": "景仁街 / 羅斯福路六段142巷口(北側)",
      "En": "Jingren St. / Ln. 142, Sec. 6, Roosevelt Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:49+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0392",
    "StationID": "0392",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南京東興路口",
      "En": "Nanjing & Dongxing Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.051489,
      "PositionLon": 121.565347
    },
    "StationAddress": {
      "Zh_tw": "南京東路五段 / 東興路口(北側)",
      "En": "Sec. 5, Nanjing E. Rd. / Dongxing Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0393",
    "StationID": "0393",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "內溝溪生態展示館",
      "En": "Neigousi Eological Exhibition Hall"
    },
    "StationPosition": {
      "PositionLat": 25.087217,
      "PositionLon": 121.623062
    },
    "StationAddress": {
      "Zh_tw": "康樂街236之3號(西北側)",
      "En": "No.236-3, Kangle St."
    },
    "BikesCapacity": 24,
    "SrcUpdateTime": "2018-11-07T09:06:46+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0394",
    "StationID": "0394",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "松德虎林街口",
      "En": "Songde & Hulin Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.038352,
      "PositionLon": 121.576248
    },
    "StationAddress": {
      "Zh_tw": "松德路71號前方",
      "En": "No.71, Songde Rd."
    },
    "BikesCapacity": 32,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0395",
    "StationID": "0395",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "安強公園",
      "En": "Anciang Park"
    },
    "StationPosition": {
      "PositionLat": 25.036844,
      "PositionLon": 121.575413
    },
    "StationAddress": {
      "Zh_tw": "虎林街212巷58號(西南側)",
      "En": "No.58, Ln. 212, Hulin St."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:22+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0396",
    "StationID": "0396",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "新東街51巷口",
      "En": "Ln.51,Xindong St."
    },
    "StationPosition": {
      "PositionLat": 25.061501,
      "PositionLon": 121.563318
    },
    "StationAddress": {
      "Zh_tw": "三民路 / 新東街51巷口(東側)",
      "En": "Sanmin Rd. / Ln. 51, Xindong St. intersection"
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:28+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0397",
    "StationID": "0397",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "劍潭海外青年活動中心",
      "En": "Chientan Overseas Youth Activity Center"
    },
    "StationPosition": {
      "PositionLat": 25.079603,
      "PositionLon": 121.5237
    },
    "StationAddress": {
      "Zh_tw": "通河街 / 通河街2巷(南側)",
      "En": "Tonghe St. / Ln. 2, Tonghe St. intersection"
    },
    "BikesCapacity": 36,
    "SrcUpdateTime": "2018-11-07T09:06:44+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0398",
    "StationID": "0398",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "聯合醫院陽明院區",
      "En": "Taipei City Hospital (Yangming Branch)"
    },
    "StationPosition": {
      "PositionLat": 25.104546,
      "PositionLon": 121.531949
    },
    "StationAddress": {
      "Zh_tw": "雨聲街105號(南側)",
      "En": "No.105, Yusheng St."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:40+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0399",
    "StationID": "0399",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "和平龍泉街口",
      "En": "Heping & Longquan Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.026404,
      "PositionLon": 121.52946
    },
    "StationAddress": {
      "Zh_tw": "和平東路一段178號(前側)",
      "En": "No.178, Sec. 1, Heping E. Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:26+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0400",
    "StationID": "0400",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "和平敦化路口",
      "En": "Heping & Dunhua Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.02444,
      "PositionLon": 121.549076
    },
    "StationAddress": {
      "Zh_tw": "和平東路三段 / 敦化南路二段口(東側)",
      "En": "Sec. 3, Heping E. Rd. / Sec. 2, Dunhua S. Rd. intersection"
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:51+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0401",
    "StationID": "0401",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "南京新生路口",
      "En": "Nanjing & Xinsheng Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.051944,
      "PositionLon": 121.527661
    },
    "StationAddress": {
      "Zh_tw": "新生北路一段 / 南京東路一段口(橋墩下方)",
      "En": "Sec. 1, Xinsheng N. Rd. / Sec. 1, Nanjing E. Rd."
    },
    "BikesCapacity": 34,
    "SrcUpdateTime": "2018-11-07T09:06:23+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0402",
    "StationID": "0402",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "下灣公園",
      "En": "Siawan Park"
    },
    "StationPosition": {
      "PositionLat": 25.065159,
      "PositionLon": 121.595611
    },
    "StationAddress": {
      "Zh_tw": "民權東路六段206巷 / 民權東路六段190巷75弄口",
      "En": "Ln. 206, Sec. 6, Minquan E. Rd. / Aly. 75, Ln. 190, Sec. 6, Minquan E. Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:25+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0403",
    "StationID": "0403",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "捷運內湖站(1號出口)",
      "En": "MRT Neihu Sta.1(Exit.1)"
    },
    "StationPosition": {
      "PositionLat": 25.083868,
      "PositionLon": 121.593929
    },
    "StationAddress": {
      "Zh_tw": "成功路四段182巷 / 成功路四段182巷6弄口(東南側)",
      "En": "Ln. 182, Sec. 4, Chenggong Rd. / Aly. 6, Ln. 182, Sec. 4, Chenggong Rd."
    },
    "BikesCapacity": 28,
    "SrcUpdateTime": "2018-11-07T09:06:31+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  },
  {
    "StationUID": "TPE0404",
    "StationID": "0404",
    "AuthorityID": "TPE",
    "StationName": {
      "Zh_tw": "民族延平路口",
      "En": "Minzu & Yanping Intersection"
    },
    "StationPosition": {
      "PositionLat": 25.068653,
      "PositionLon": 121.510569
    },
    "StationAddress": {
      "Zh_tw": "民族西路 310 號前方",
      "En": "No.310, Minzu W. Rd."
    },
    "BikesCapacity": 30,
    "SrcUpdateTime": "2018-11-07T09:06:16+08:00",
    "UpdateTime": "2018-11-07T09:08:47+08:00"
  }
]


# count how many stations' names have been changed
unknown = []

for i in name:
	inDic = False
	for j in a:
		if i == j['StationName']['Zh_tw']:
			inDic = True
			break
	if inDic == False:
		unknown.append(i)

print(unknown)
print(len(unknown))