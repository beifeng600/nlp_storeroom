nlp_storeroom
=============

NLP的一些公开资料，有些是别人原始分享的，有些是处理了一下。

文件列表：


-nlp_storeroom/

	--dict/
		---zh/
			现代汉语词典_第5版_词表.txt,	// 共54343条，2005年6月，第五版，
			汉语成语词典_词表_23889条.txt,	// 共23889条，未知版本
			
			----character set
				GB2312汉字表_6763.txt,	//	6763条，《信息交换用汉字编码字符集·基本集》，GB2312或GB2312-80。其中的汉字表。
				GBK汉字表_21003.txt,	//	21003条，GBK，汉字内码扩展规范。Chinese Internal Code Specification.其中汉字表。
				Big5汉字表_13060.txt,	//	13060条，Big5 (Traditional Chinese) character code table.其中汉字表，最后两个字“兀嗀”是重复编码。
				Unicode中文汉字_20902.txt,	// 20902条，Unicode其中的汉字表。
				
				-----相关文档	（汉字编码相关的文档。）
					通用规范汉字表，2013年，参见http://www.gov.cn/zwgk/2013-08/19/content_2469793.htm
					
				-----繁简体
					简化字总表(1986)_2276条.txt,	// 共2276条。简化字总表，1986年新版
			----分类词库
				2014年全国高等学校名单_2542所.txt,    // 截至2014年7月9日
				我国县及县以上行政区划代码-截止2013年8月31日.txt,    //共3514个。
				联合国会员国列表.txt,    //193个
				
			
	--corpus/
		---bilingual parallel corpus
			外国人名foreignNames_list_39687.txt, 	// 外国人名，中英对照的，共39687条
			1500en_zh.txt，		// 英汉双语句对齐语料库，1500句对
	
	--tools/
		---分句
			CutFile_ZH.py,    //中文分句工具，python
		
