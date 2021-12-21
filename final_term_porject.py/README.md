설명
-주가만을 이용해 다음날의 주가를 예측할 수 있는가를 파악하기 위한 프로그램을 제작함.

결과
![samsung](./img/samsung.png)

단점
-주가를 예측하는 모습보다 전날의 가격을 따라가는 모습이 나타남

해결법
-거래량, 매수세, 매도세 등등의 다른 값들을 이용하면 조금 더 정확한 예측이 가능할 것 같다.

제작과정
1.야후 파이낸스에서 데이터를 download한다.  
2.tenserflow, Keara 라이브러리 import후 다운받은 csv파일을 불러온다.  
3.고가, 저가의 중간 값이 mid_prices를 구한다.  
4.50개의 데이터를 연속적으로 읽고 다음 데이터를 파악하는 RNN구조의 데이터를 만든다.  
5.window 50개의 저장된 데이터를 정규화 하여 window[0]을 기준으로 나눈다.  
6.헤당 데이터의 90%를 train데이터 나머지 10%를 test데이터로 사용한다.  
7.LSTM모델을 사용하여 머신러닝 모델을 제작한다.  
8.모델 피팅.  
9.matpliot을 통해 실제모델과 예측모델의 차이를 살핀다.  
  

참고자료
 * https://datamasters.co.kr/25 (라이브러리 설치)
 * https://www.olis.or.kr/license/compareGuide.do (라이센스 확인)
 * https://www.oss.kr/oss_license (라이센스 확인)
 * https://github.com/kairess/stock_crypto_price_prediction (참고자료)
 * https://12soso12.tistory.com/84 (참고자료)
 * https://www.youtube.com/watch?v=sG_WeGbZ9A4 (참고자료)
 * https://www.youtube.com/watch?v=yZoHlkCbNoM&t=245s (참고자료)
 * https://www.delftstack.com/ko/howto/matplotlib/how-to-add-title-to-subplots-in-matplotlib/ (서브플롯)
 * http://daplus.net/python-서브-플롯에-대한-pyplot-좌표축-레이블/ (서브플롯)
 * https://data-make.tistory.com/137 (서브플롯)

라이센스
 * https://www.apache.org/licenses/LICENSE-2.0

데이타 얻는곳
 * https://finance.yahoo.com/quote/005930.KS/history?p=005930.KS
