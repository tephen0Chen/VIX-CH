'''
Author:咸鱼小易EEY gzh:finance褪黑素
Date: 2024-04-06 20:00:00
LastEditors: 咸鱼小易EEY gzh:finance褪黑素
LastEditTime: 2024-04-06 20:00:00
Description: 
'''

import pandas as pd
import numpy as np


def trans_ser2datetime(ser: pd.Series) -> pd.Series:
    """将ser类型转为datetime

    Args:
        ser (pd.Series): _description_

    Raises:
        TypeError: _description_

    Returns:
        pd.Series: _description_
    """
    if not isinstance(ser, pd.Series):

        raise TypeError('ser必须为pd.Series')

    if (ser.dtype != np.dtype('O')) or (ser.dtype != np.dtype('<M8[ns]')):

        ser = pd.to_datetime(ser)

    return ser