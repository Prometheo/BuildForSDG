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

  severeCasesByRequestedTime_best = int(15 * (infectionsByRequestedTime_best/100))
  severeCasesByRequestedTime_severe = int(15 * (infectionsByRequestedTime_best/100))

  bedAvailablePercent = int(35*(data['totalHospitalBeds']/100))
  hospitalBedsByRequestedTime_best = bedAvailablePercent - severeCasesByRequestedTime_best
  hospitalBedsByRequestedTime_severe = bedAvailablePercent - severeCasesByRequestedTime_severe

  fivePercentInfections_best = int(5 * (infectionsByRequestedTime_best/100))
  fivePercentInfections_severe = int(5 * (infectionsByRequestedTime_best/100))

  twopercentInfections_best = int(2 * (infectionsByRequestedTime_best/100))
  twopercentInfections_severe = int(2 * (infectionsByRequestedTime_best/100))

  treasury_best = int(infectionsByRequestedTime_best * 0.71 * 5 * days)
  treasury_severe = int(infectionsByRequestedTime_severe * 0.71 * 5 * days)
  
  data = {
    'data': data,
    'impact': {
      'currentlyInfected': currentlyInfected_best,
      'infectionsByRequestedTime': infectionsByRequestedTime_best,
      'severeCasesByRequestedTime': severeCasesByRequestedTime_best,
      'hospitalBedsByRequestedTime': hospitalBedsByRequestedTime_best,
      'casesForICUByRequestedTime': fivePercentInfections_best,
      'casesForVentilatorsByRequestedTime': twopercentInfections_best,
      'dollarsInFlight': treasury_best
    },
    'severeImpact': {
      'currentlyInfected': currentlyInfected_severe,
      'infectionsByRequestedTime': infectionsByRequestedTime_severe,
      'severeCasesByRequestedTime': severeCasesByRequestedTime_severe,
      'hospitalBedsByRequestedTime': hospitalBedsByRequestedTime_severe,
      'casesForICUByRequestedTime': fivePercentInfections_severe,
      'casesForVentilatorsByRequestedTime': twopercentInfections_severe,
      'dollarsInFlight': treasury_severe 
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