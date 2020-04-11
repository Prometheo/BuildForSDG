def estimator(data):
  currentlyInfected_best = data['reportedCases'] * 10
  currentlyInfected_severe = data['reportedCases'] * 50
  if data['periodType'] == 'days':
    days = data['timeToElapse']
    factor = int(days/3)
  elif  data['periodType'] == 'weeks':
    days = data['timeToElapse']*7
    factor = int(days/3)
  else:
    days = data['timeToElapse']*30
    factor = int(days/3)
  infectionsByRequestedTime_best = currentlyInfected_best * (2**factor)
  infectionsByRequestedTime_severe = currentlyInfected_severe * (2**factor)

  severeCasesByRequestedTime_best = (15 * (infectionsByRequestedTime_best/100))
  severeCasesByRequestedTime_severe = (15 * (infectionsByRequestedTime_severe/100))

  bedAvailablePercent = (35*(data['totalHospitalBeds']/100))
  hospitalBedsByRequestedTime_best = bedAvailablePercent - severeCasesByRequestedTime_best
  hospitalBedsByRequestedTime_severe = bedAvailablePercent - severeCasesByRequestedTime_severe

  fivePercentInfections_best = (5 * (infectionsByRequestedTime_best/100))
  fivePercentInfections_severe = (5 * (infectionsByRequestedTime_best/100))

  twopercentInfections_best = (2 * (infectionsByRequestedTime_best/100))
  twopercentInfections_severe = (2 * (infectionsByRequestedTime_best/100))

  treasury_best = (infectionsByRequestedTime_best * 0.71 * 5 * days)
  treasury_severe = (infectionsByRequestedTime_severe * 0.71 * 5 * days)
  
  data = {
    'data': data,
    'impact': {
      'currentlyInfected': int(currentlyInfected_best),
      'infectionsByRequestedTime': int(infectionsByRequestedTime_best),
      'severeCasesByRequestedTime': int(severeCasesByRequestedTime_best),
      'hospitalBedsByRequestedTime': int(hospitalBedsByRequestedTime_best),
      'casesForICUByRequestedTime': int(fivePercentInfections_best),
      'casesForVentilatorsByRequestedTime': int(twopercentInfections_best),
      'dollarsInFlight': int(treasury_best)
    },
    'severeImpact': {
      'currentlyInfected': int(currentlyInfected_severe),
      'infectionsByRequestedTime': int(infectionsByRequestedTime_severe),
      'severeCasesByRequestedTime': int(severeCasesByRequestedTime_severe),
      'hospitalBedsByRequestedTime': int(hospitalBedsByRequestedTime_severe),
      'casesForICUByRequestedTime': int(fivePercentInfections_severe),
      'casesForVentilatorsByRequestedTime': int(twopercentInfections_severe),
      'dollarsInFlight': int(treasury_severe) 
    }

    }

  return data


# data = {
# 'region': {
# 'name': "Africa",
# 'avgAge': 19.7,
# 'avgDailyIncomeInUSD': 5,
# 'avgDailyIncomePopulation': 0.71
# },
# 'periodType': "days",
# 'timeToElapse': 58,
# 'reportedCases': 674,
# 'population': 66622705,
# 'totalHospitalBeds': 1380614
# }