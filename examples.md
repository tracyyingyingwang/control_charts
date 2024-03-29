# Examples

# XmR control charts

## Dataframe with single column and index

Download [xmr.csv](https://drive.google.com/open?id=0BzrdQfHR2I5DRld4MndVT2R0dEk) if you need and example file.

    from pathlib import Path

    import pandas as pd
    import matplotlib.pyplot as plt

    from datasense import X
    from datasense import mR

    chart_data = pd.read_csv(Path(__file__).parent / 'xmr.csv',
                            index_col='Sample').iloc[:, 0:]
    x = X(chart_data)
    print('X chart')
    print('Upper control limit', x.ucl, sep=' = ')
    print('Average moving range', x.mean, sep=' = ')
    print('Lower control limit', x.lcl, sep=' = ')
    print(f'Sigma(X)', x.sigma, sep=' = ')
    for i in range(-3, 4):
        print(f'{i} Sigma', ' '.join(map(str, [x.sigmas[i]])), sep=' = ')
    ax1 = x.ax
    ax1.set_title('X control chart' + '\n' 'Subtitle')
    ax1.set_ylabel('Response (units)')
    ax1.set_xlabel('X axis label')
    plt.show()
    mr = mR(chart_data)
    print('mR chart')
    print('Upper control limit', mr.ucl, sep=' = ')
    print('Average moving range', mr.mean, sep=' = ')
    print('Lower control limit', mr.lcl, sep=' = ')
    print(f'Sigma(X)', mr.sigma, sep=' = ')
    for i in range(-3, 4):
        print(f'{i} Sigma', ' '.join(map(str, [mr.sigmas[i]])), sep=' = ')
    ax2 = mr.ax
    ax2.set_title('mR control chart' + '\n' 'Subtitle')
    ax2.set_ylabel('Response (units)')
    ax2.set_xlabel('X axis label')
    plt.show()

## Dataframe with multiple columns and index

TBD

# XbarR control charts

## Dataframe with single column and index

TBD

## Dataframe with multiple columns and index

TBD
