PERIODS={
  22:'Late evening',20:'Evening',18:'Early evening',
  16:'Late day',14:'Day',12:'Early day',
  10:'Late morning',8:'Morning',6:'Early morning',
  4:'Late night',2:'Night',0:'Early night',
}

def get(hourp):
  for hour in PERIODS:
    if hourp>=hour:
      return PERIODS[hour]
  raise Exception(f'No known period for {hourp}')
