import yfinance as yf
import pandas as pd

# Lista de tickers de las acciones chilenas
tickers_chilenos = ['CENCOSUD.SN', 'ENELAM.SN', 'FALABELLA.SN', 'LTM.SN', 'ENELCHILE.SN',
                    'BSANTANDER.SN', 'SQM.SN', 'ENELGXCH.SN', 'CAP.SN', 'ANDINA-B.SN']

# Lista para almacenar los múltiplos financieros
multiples_chilenos = []

# Función para obtener datos y calcular múltiplos
def obtener_multiplos_chilenos(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    # Calcular múltiplos
    pe_ratio = info.get('forwardPE', 'N/A')
    pb_ratio = info.get('priceToBook', 'N/A')
    market_cap = info.get('marketCap', 'N/A')
    dividend_yield = info.get('dividendYield', 'N/A')
    roe = info.get('returnOnEquity', 'N/A')

    multiples_chilenos.append({
        'Ticker': ticker,
        'P/E Ratio': pe_ratio,
        'P/B Ratio': pb_ratio,
        'Market Cap': market_cap,
        'Dividend Yield': dividend_yield,
        'ROE': roe
    })

# Obtener datos para cada ticker chileno
for ticker in tickers_chilenos:
    try:
        obtener_multiplos_chilenos(ticker)
    except Exception as e:
        print(f"Error al obtener los datos de {ticker}: {e}")

# Convertir la lista de múltiplos a un DataFrame de pandas para una mejor visualización
df_multiples_chilenos = pd.DataFrame(multiples_chilenos)

# Filtrar empresas con datos válidos
df_multiples_chilenos = df_multiples_chilenos[df_multiples_chilenos['P/E Ratio'] != 'N/A']
df_multiples_chilenos = df_multiples_chilenos[df_multiples_chilenos['ROE'] != 'N/A']
df_multiples_chilenos = df_multiples_chilenos[df_multiples_chilenos['P/E Ratio'].notna()]
df_multiples_chilenos = df_multiples_chilenos[df_multiples_chilenos['ROE'].notna()]

# Convertir a tipos numéricos
df_multiples_chilenos['P/E Ratio'] = pd.to_numeric(df_multiples_chilenos['P/E Ratio'], errors='coerce')
df_multiples_chilenos['ROE'] = pd.to_numeric(df_multiples_chilenos['ROE'], errors='coerce')

# Filtrar empresas rentables (P/E Ratio > 0 y ROE > 0)
empresas_rentables_chilenas = df_multiples_chilenos[(df_multiples_chilenos['P/E Ratio'] > 0) & (df_multiples_chilenos['ROE'] > 0)]

# Ordenar por P/E Ratio y ROE
empresas_rentables_chilenas = empresas_rentables_chilenas.sort_values(by=['P/E Ratio', 'ROE'], ascending=[True, False])

# Mostrar los mejores resultados arriba y los peores abajo
print(empresas_rentables_chilenas)

# Guardar los resultados en un archivo CSV
empresas_rentables_chilenas.to_csv('empresas_rentables_chilenas.csv', index=False)
