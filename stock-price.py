from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

def is_good_response(response):
    content_type = response.headers["Content-Type"].lower()
    return (response.status_code == 200 
            and content_type is not None
            and content_type.find("json") > -1)

def get_data(url):
    headers = {
        'Ocp-Apim-Subscription-Key': 'd1b9ee5fcf40434ab51854beecb75c6f',
        'Content-Type': 'application/json',
        'Referer' : 'https://analises.xpi.com.br/fundamentalista/empresas/',
        'Origin': 'https://analises.xpi.com.br'
    }

    with closing(get(url, stream=False, headers=headers)) as response:
        if (is_good_response(response)):
            return response.json()
        else:
            return None

stocks = [{'code': 'FRTA3', 'data': None},
{'code': 'SLCE3', 'data': None},
{'code': 'TESA3', 'data': None},
{'code': 'SAPR4', 'data': None},
{'code': 'SAPR11', 'data': None},
{'code': 'SAPR3', 'data': None},
{'code': 'CSMG3', 'data': None},
{'code': 'SBSP3', 'data': None},
{'code': 'JBSS3', 'data': None},
{'code': 'BRFS3', 'data': None},
{'code': 'BSEV3', 'data': None},
{'code': 'BEEF3', 'data': None},
{'code': 'MNPR3', 'data': None},
{'code': 'MRFG3', 'data': None},
{'code': 'JOPA4', 'data': None},
{'code': 'JOPA3', 'data': None},
{'code': 'CSAN3', 'data': None},
{'code': 'CAML3', 'data': None},
{'code': 'BAUH4', 'data': None},
{'code': 'SMTO3', 'data': None},
{'code': 'MDIA3', 'data': None},
{'code': 'ABEV3', 'data': None},
{'code': 'BTOW3', 'data': None},
{'code': 'VVAR3', 'data': None},
{'code': 'AMAR3', 'data': None},
{'code': 'LLIS3', 'data': None},
{'code': 'CGRA3', 'data': None},
{'code': 'CGRA4', 'data': None},
{'code': 'HYPE3', 'data': None},
{'code': 'GUAR3', 'data': None},
{'code': 'GUAR4', 'data': None},
{'code': 'LREN3', 'data': None},
{'code': 'ARZZ3', 'data': None},
{'code': 'MGLU3', 'data': None},
{'code': 'LAME3', 'data': None},
{'code': 'LAME4', 'data': None},
{'code': 'WLMM4', 'data': None},
{'code': 'WLMM3', 'data': None},
{'code': 'PFRM3', 'data': None},
{'code': 'BPHA3', 'data': None},
{'code': 'PNVL4', 'data': None},
{'code': 'PCAR4', 'data': None},
{'code': 'PCAR3', 'data': None},
{'code': 'CRFB3', 'data': None},
{'code': 'PNVL3', 'data': None},
{'code': 'RADL3', 'data': None},
{'code': 'ITEC3', 'data': None},
{'code': 'POSI3', 'data': None},
{'code': 'CYRE3', 'data': None},
{'code': 'CALI4', 'data': None},
{'code': 'LPSB3', 'data': None},
{'code': 'DIRR3', 'data': None},
{'code': 'RDNI3', 'data': None},
{'code': 'MILS3', 'data': None},
{'code': 'CRDE3', 'data': None},
{'code': 'EVEN3', 'data': None},
{'code': 'BBRK3', 'data': None},
{'code': 'HBOR3', 'data': None},
{'code': 'AZEV3', 'data': None},
{'code': 'VIVR3', 'data': None},
{'code': 'TCSA3', 'data': None},
{'code': 'JFEN3', 'data': None},
{'code': 'TCNO3', 'data': None},
{'code': 'TCNO4', 'data': None},
{'code': 'GFSA3', 'data': None},
{'code': 'AZEV4', 'data': None},
{'code': 'RSID3', 'data': None},
{'code': 'ETER3', 'data': None},
{'code': 'MEND5', 'data': None},
{'code': 'MEND6', 'data': None},
{'code': 'PDGR3', 'data': None},
{'code': 'SOND6', 'data': None},
{'code': 'PTBL3', 'data': None},
{'code': 'SOND5', 'data': None},
{'code': 'JHSF3', 'data': None},
{'code': 'MRVE3', 'data': None},
{'code': 'TEND3', 'data': None},
{'code': 'TRIS3', 'data': None},
{'code': 'EZTC3', 'data': None},
{'code': 'HAGA4', 'data': None},
{'code': 'HAGA3', 'data': None},
{'code': 'SMLS3', 'data': None},
{'code': 'KROT3', 'data': None},
{'code': 'MPLU3', 'data': None},
{'code': 'ESTC3', 'data': None},
{'code': 'SEER3', 'data': None},
{'code': 'MOVI3', 'data': None},
{'code': 'LCAM3', 'data': None},
{'code': 'RENT3', 'data': None},
{'code': 'ANIM3', 'data': None},
{'code': 'MTIG4', 'data': None},
{'code': 'ELET5', 'data': None},
{'code': 'ELPL3', 'data': None},
{'code': 'ELET6', 'data': None},
{'code': 'ELET3', 'data': None},
{'code': 'CEBR5', 'data': None},
{'code': 'CEBR6', 'data': None},
{'code': 'CEED4', 'data': None},
{'code': 'CEED3', 'data': None},
{'code': 'RNEW3', 'data': None},
{'code': 'RNEW11', 'data': None},
{'code': 'RNEW4', 'data': None},
{'code': 'EMAE4', 'data': None},
{'code': 'TRPL4', 'data': None},
{'code': 'TRPL3', 'data': None},
{'code': 'CPLE3', 'data': None},
{'code': 'TAEE11', 'data': None},
{'code': 'ENBR3', 'data': None},
{'code': 'EKTR3', 'data': None},
{'code': 'CPLE6', 'data': None},
{'code': 'EKTR4', 'data': None},
{'code': 'COCE3', 'data': None},
{'code': 'CLSC4', 'data': None},
{'code': 'ENEV3', 'data': None},
{'code': 'COCE5', 'data': None},
{'code': 'CLSC3', 'data': None},
{'code': 'CSRN5', 'data': None},
{'code': 'CSRN3', 'data': None},
{'code': 'CEPE5', 'data': None},
{'code': 'CEEB3', 'data': None},
{'code': 'CEPE6', 'data': None},
{'code': 'CELP7', 'data': None},
{'code': 'AFLT3', 'data': None},
{'code': 'EGIE3', 'data': None},
{'code': 'CMIG4', 'data': None},
{'code': 'TIET4', 'data': None},
{'code': 'TIET11', 'data': None},
{'code': 'ENGI4', 'data': None},
{'code': 'TIET3', 'data': None},
{'code': 'CPFE3', 'data': None},
{'code': 'EQTL3', 'data': None},
{'code': 'LIPR3', 'data': None},
{'code': 'ALUP4', 'data': None},
{'code': 'CMIG3', 'data': None},
{'code': 'ALUP11', 'data': None},
{'code': 'ENGI11', 'data': None},
{'code': 'ALUP3', 'data': None},
{'code': 'GEPA3', 'data': None},
{'code': 'ENMT3', 'data': None},
{'code': 'CBEE3', 'data': None},
{'code': 'OMGE3', 'data': None},
{'code': 'ENMT4', 'data': None},
{'code': 'CELP5', 'data': None},
{'code': 'GEPA4', 'data': None},
{'code': 'LIGT3', 'data': None},
{'code': 'ENGI3', 'data': None},
{'code': 'REDE3', 'data': None},
{'code': 'CESP3', 'data': None},
{'code': 'CESP6', 'data': None},
{'code': 'CESP5', 'data': None},
{'code': 'CPRE3', 'data': None},
{'code': 'FRIO3', 'data': None},
{'code': 'CCPR3', 'data': None},
{'code': 'AHEB3', 'data': None},
{'code': 'BRML3', 'data': None},
{'code': 'GSHP3', 'data': None},
{'code': 'CORR4', 'data': None},
{'code': 'AGRO3', 'data': None},
{'code': 'SCAR3', 'data': None},
{'code': 'SSBR3', 'data': None},
{'code': 'LOGG3', 'data': None},
{'code': 'IGTA3', 'data': None},
{'code': 'MULT3', 'data': None},
{'code': 'ALSC3', 'data': None},
{'code': 'BRPR3', 'data': None},
{'code': 'PINE4', 'data': None},
{'code': 'IDVL3', 'data': None},
{'code': 'IDVL4', 'data': None},
{'code': 'RPAD5', 'data': None},
{'code': 'RPAD6', 'data': None},
{'code': 'RPAD3', 'data': None},
{'code': 'BRGE12', 'data': None},
{'code': 'BRGE5', 'data': None},
{'code': 'MERC4', 'data': None},
{'code': 'BRGE3', 'data': None},
{'code': 'BNBR3', 'data': None},
{'code': 'BRGE8', 'data': None},
{'code': 'BPAR3', 'data': None},
{'code': 'BRGE7', 'data': None},
{'code': 'BRGE11', 'data': None},
{'code': 'MERC3', 'data': None},
{'code': 'BMEB4', 'data': None},
{'code': 'BMEB3', 'data': None},
{'code': 'CRIV3', 'data': None},
{'code': 'BEES3', 'data': None},
{'code': 'BEES4', 'data': None},
{'code': 'BGIP3', 'data': None},
{'code': 'BGIP4', 'data': None},
{'code': 'CRIV4', 'data': None},
{'code': 'ABCB4', 'data': None},
{'code': 'BRSR3', 'data': None},
{'code': 'BRSR5', 'data': None},
{'code': 'BRSR6', 'data': None},
{'code': 'BRIV3', 'data': None},
{'code': 'ITSA4', 'data': None},
{'code': 'BRIV4', 'data': None},
{'code': 'BBAS3', 'data': None},
{'code': 'BRGE6', 'data': None},
{'code': 'BBDC3', 'data': None},
{'code': 'ITSA3', 'data': None},
{'code': 'SANB11', 'data': None},
{'code': 'SANB3', 'data': None},
{'code': 'ITUB3', 'data': None},
{'code': 'SANB4', 'data': None},
{'code': 'BSLI4', 'data': None},
{'code': 'BBDC4', 'data': None},
{'code': 'ITUB4', 'data': None},
{'code': 'BPAN4', 'data': None},
{'code': 'BAZA3', 'data': None},
{'code': 'BPAC5', 'data': None},
{'code': 'BMIN3', 'data': None},
{'code': 'BMIN4', 'data': None},
{'code': 'BPAC11', 'data': None},
{'code': 'BPAC3', 'data': None},
{'code': 'BIDI4', 'data': None},
{'code': 'CGAS3', 'data': None},
{'code': 'CGAS5', 'data': None},
{'code': 'CEGR3', 'data': None},
{'code': 'BAHI3', 'data': None},
{'code': 'BTTL3', 'data': None},
{'code': 'GPIV33', 'data': None},
{'code': 'HBTS5', 'data': None},
{'code': 'JBDU3', 'data': None},
{'code': 'JBDU4', 'data': None},
{'code': 'TRPN3', 'data': None},
{'code': 'BRAP3', 'data': None},
{'code': 'BRAP4', 'data': None},
{'code': 'UGPA3', 'data': None},
{'code': 'MOAR3', 'data': None},
{'code': 'MEAL3', 'data': None},
{'code': 'HOOT4', 'data': None},
{'code': 'BKBR3', 'data': None},
{'code': 'MSPA3', 'data': None},
{'code': 'MSPA4', 'data': None},
{'code': 'FIBR3', 'data': None},
{'code': 'EUCA4', 'data': None},
{'code': 'DTEX3', 'data': None},
{'code': 'EUCA3', 'data': None},
{'code': 'KLBN4', 'data': None},
{'code': 'KLBN11', 'data': None},
{'code': 'RANI3', 'data': None},
{'code': 'RANI4', 'data': None},
{'code': 'SUZB3', 'data': None},
{'code': 'KLBN3', 'data': None},
{'code': 'KEPL3', 'data': None},
{'code': 'NORD3', 'data': None},
{'code': 'FJTA3', 'data': None},
{'code': 'FJTA4', 'data': None},
{'code': 'INEP4', 'data': None},
{'code': 'INEP3', 'data': None},
{'code': 'LUPA3', 'data': None},
{'code': 'BDLL4', 'data': None},
{'code': 'EALT4', 'data': None},
{'code': 'EALT3', 'data': None},
{'code': 'ROMI3', 'data': None},
{'code': 'SHUL4', 'data': None},
{'code': 'MTSA4', 'data': None},
{'code': 'WEGE3', 'data': None},
{'code': 'BALM3', 'data': None},
{'code': 'BALM4', 'data': None},
{'code': 'MAGG3', 'data': None},
{'code': 'EMBR3', 'data': None},
{'code': 'MWET3', 'data': None},
{'code': 'MWET4', 'data': None},
{'code': 'PLAS3', 'data': None},
{'code': 'RCSL4', 'data': None},
{'code': 'RSUL4', 'data': None},
{'code': 'FRAS3', 'data': None},
{'code': 'LEVE3', 'data': None},
{'code': 'TUPY3', 'data': None},
{'code': 'POMO3', 'data': None},
{'code': 'POMO4', 'data': None},
{'code': 'RAPT3', 'data': None},
{'code': 'MYPK3', 'data': None},
{'code': 'RAPT4', 'data': None},
{'code': 'SEDU3', 'data': None},
{'code': 'SLED3', 'data': None},
{'code': 'SLED4', 'data': None},
{'code': 'CCXC3', 'data': None},
{'code': 'MMXM3', 'data': None},
{'code': 'VALE3', 'data': None},
{'code': 'TELB4', 'data': None},
{'code': 'TELB3', 'data': None},
{'code': 'DMMO3', 'data': None},
{'code': 'OGXP3', 'data': None},
{'code': 'OSXB3', 'data': None},
{'code': 'RPMG3', 'data': None},
{'code': 'QGEP3', 'data': None},
{'code': 'BRDT3', 'data': None},
{'code': 'PETR4', 'data': None},
{'code': 'PETR3', 'data': None},
{'code': 'PRIO3', 'data': None},
{'code': 'IRBR3', 'data': None},
{'code': 'CSAB4', 'data': None},
{'code': 'BBSE3', 'data': None},
{'code': 'CSAB3', 'data': None},
{'code': 'WIZS3', 'data': None},
{'code': 'SULA4', 'data': None},
{'code': 'SULA11', 'data': None},
{'code': 'PSSA3', 'data': None},
{'code': 'PEAB3', 'data': None},
{'code': 'SULA3', 'data': None},
{'code': 'PEAB4', 'data': None},
{'code': 'ADHM3', 'data': None},
{'code': 'BOBR4', 'data': None},
{'code': 'NATU3', 'data': None},
{'code': 'IDNT3', 'data': None},
{'code': 'LINX3', 'data': None},
{'code': 'TOTS3', 'data': None},
{'code': 'SQIA3', 'data': None},
{'code': 'NUTR3', 'data': None},
{'code': 'FHER3', 'data': None},
{'code': 'CRPG3', 'data': None},
{'code': 'CRPG5', 'data': None},
{'code': 'CRPG6', 'data': None},
{'code': 'GPCP3', 'data': None},
{'code': 'ELEK4', 'data': None},
{'code': 'ELEK3', 'data': None},
{'code': 'UNIP6', 'data': None},
{'code': 'UNIP3', 'data': None},
{'code': 'UNIP5', 'data': None},
{'code': 'BRKM6', 'data': None},
{'code': 'BRKM3', 'data': None},
{'code': 'BRKM5', 'data': None},
{'code': 'GBIO33', 'data': None},
{'code': 'BIOM3', 'data': None},
{'code': 'HAPV3', 'data': None},
{'code': 'QUAL3', 'data': None},
{'code': 'FLRY3', 'data': None},
{'code': 'PARD3', 'data': None},
{'code': 'OFSA3', 'data': None},
{'code': 'ODPV3', 'data': None},
{'code': 'DASA3', 'data': None},
{'code': 'GNDI3', 'data': None},
{'code': 'AALR3', 'data': None},
{'code': 'DTCY3', 'data': None},
{'code': 'LIQO3', 'data': None},
{'code': 'CARD3', 'data': None},
{'code': 'VLID3', 'data': None},
{'code': 'CIEL3', 'data': None},
{'code': 'B3SA3', 'data': None},
{'code': 'TKNO4', 'data': None},
{'code': 'PMAM3', 'data': None},
{'code': 'MGEL4', 'data': None},
{'code': 'FBMC4', 'data': None},
{'code': 'CSNA3', 'data': None},
{'code': 'PATI3', 'data': None},
{'code': 'FESA4', 'data': None},
{'code': 'FESA3', 'data': None},
{'code': 'GOAU4', 'data': None},
{'code': 'GOAU3', 'data': None},
{'code': 'PATI4', 'data': None},
{'code': 'GGBR3', 'data': None},
{'code': 'GGBR4', 'data': None},
{'code': 'USIM5', 'data': None},
{'code': 'USIM6', 'data': None},
{'code': 'USIM3', 'data': None},
{'code': 'MNDL3', 'data': None},
{'code': 'CTKA3', 'data': None},
{'code': 'CTKA4', 'data': None},
{'code': 'TXRX4', 'data': None},
{'code': 'TEKA3', 'data': None},
{'code': 'TEKA4', 'data': None},
{'code': 'CEDO4', 'data': None},
{'code': 'CEDO3', 'data': None},
{'code': 'CAMB4', 'data': None},
{'code': 'ECPR3', 'data': None},
{'code': 'CTNM4', 'data': None},
{'code': 'CTNM3', 'data': None},
{'code': 'CTSA3', 'data': None},
{'code': 'DOHL4', 'data': None},
{'code': 'DOHL3', 'data': None},
{'code': 'CTSA4', 'data': None},
{'code': 'PTNT4', 'data': None},
{'code': 'VULC3', 'data': None},
{'code': 'GRND3', 'data': None},
{'code': 'HGTX3', 'data': None},
{'code': 'PTNT3', 'data': None},
{'code': 'ALPA3', 'data': None},
{'code': 'ALPA4', 'data': None},
{'code': 'SGPS3', 'data': None},
{'code': 'TECN3', 'data': None},
{'code': 'OIBR4', 'data': None},
{'code': 'OIBR3', 'data': None},
{'code': 'VIVT3', 'data': None},
{'code': 'VIVT4', 'data': None},
{'code': 'JPSA3', 'data': None},
{'code': 'ATOM3', 'data': None},
{'code': 'TIMP3', 'data': None},
{'code': 'LOGN3', 'data': None},
{'code': 'GOLL4', 'data': None},
{'code': 'TPIS3', 'data': None},
{'code': 'LUXM4', 'data': None},
{'code': 'TGMA3', 'data': None},
{'code': 'ECOR3', 'data': None},
{'code': 'CCRO3', 'data': None},
{'code': 'WSON33', 'data': None},
{'code': 'AZUL4', 'data': None},
{'code': 'JSLG3', 'data': None},
{'code': 'RLOG3', 'data': None},
{'code': 'RAIL3', 'data': None},
{'code': 'STBP3', 'data': None},
{'code': 'UCAS3', 'data': None},
{'code': 'SPRI3', 'data': None},
{'code': 'SPRI5', 'data': None},
{'code': 'HETA4', 'data': None},
{'code': 'IGBR3', 'data': None},
{'code': 'NAFG4', 'data': None},
{'code': 'NAFG3', 'data': None},
{'code': 'WHRL3', 'data': None},
{'code': 'WHRL4', 'data': None},
{'code': 'TOYB3', 'data': None},
{'code': 'TOYB4', 'data': None},
{'code': 'ESTR4', 'data': None},
{'code': 'CVCB3', 'data': None},
{'code': 'SHOW3', 'data': None},
{'code': 'BMKS3', 'data': None}]

def prepare_csv(json_data):
    data_separator = ';'
    return (json_data['ativo'] + data_separator 
    + json_data['ultimoPreco'] + data_separator
    + json_data['quantidade'] + data_separator
    + json_data['oscilacao'] + data_separator 
    + json_data['tendencia'] + data_separator 
    + json_data['hora'] + data_separator 
    + json_data['qtdOfertaCompra'] + data_separator 
    + json_data['vlOfertaCompra'] + data_separator 
    + json_data['qtdOfertaVenda'] + data_separator 
    + json_data['vlOfertaVenda'] + data_separator 
    + json_data['qtdNegociada'] + data_separator 
    + json_data['volumeNegocios'] + data_separator 
    + json_data['negocios'] + data_separator 
    + json_data['statusPapel'] + data_separator 
    + json_data['precoTeoricoAbertura'] + data_separator 
    + json_data['qtdTeoricaAberrtura'] + data_separator 
    + json_data['dtCotacao'] + data_separator 
    + json_data['fechamentoAnterior'] + data_separator 
    + json_data['precoAbertura'] + data_separator 
    + json_data['precoMinimo'] + data_separator 
    + json_data['precoMedio'] + data_separator 
    + json_data['precoMaximo'] + data_separator 
    + json_data['dtFechamento'] + data_separator 
    + json_data['vlFechamento'])

def get_stock_data(stock_code):
    response_data = get_data('https://api.xpi.com.br/variable-income/quote/{0}'.format(stock_code))
    if (response_data is not None):
        return prepare_csv(response_data)
    else:
        return None

fileData = open("stock-price.csv","w")
fileData.write('ativo; \
ultimoPreco;\
quantidade;\
oscilacao;\
tendencia;\
hora;\
qtdOfertaCompra;\
vlOfertaCompra;\
qtdOfertaVenda;\
vlOfertaVenda;\
qtdNegociada;\
volumeNegocios;\
negocios;\
statusPapel;\
precoTeoricoAbertura;\
qtdTeoricaAberrtura;\
dtCotacao;\
fechamentoAnterior;\
precoAbertura;\
precoMinimo;\
precoMedio;\
precoMaximo;\
dtFechamento;\
vlFechamento\n')

for stock in stocks:
    #sleep(1)
    print('stock: ' + str(stock['code']))
    stock['data'] = get_stock_data(stock['code'])
    fileData.write(stock['data'] + '\n') 
    print('stock: ' + str(stock['data']))
    

    