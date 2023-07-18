import requests
import os
import numpy as np
import seaborn as sns

class BerryStats:
  """
    A class used to retrieve info and calculate stats for the Berry elements in the Pokeapi.

    ...

    Attributes
    ----------
    _complete_berry_url_list : list
        List of single berry url elements with format {'name': <Berry name:str>, 'url': <Berry url:str>}
    _base_url : str
        the base url for berry info retrieval
    _berry_growth_times : list
        list of ints containing the growth times for each berry
    _berry_names : list
        list of string containing the names of the berries

    Methods
    -------
    fetch_stats()
        Prints the animals name and what sound it makes
    calculate_stats()
        Calculates the stats based on the fetched values and returns the results
    generate_histogram_image()
        Generates a plot based on the frequency histogram of growth times for all Berries and returns the path of the image
  """
  
  def __init__(self, url:str) -> None:
    self._base_url = url
    self._complete_berry_url_list = []

  def _add_elements_from_list(self, result_list: list) -> None:
    """
    Parameters
    ----------
    result_list : list
        List of single berry url elements with format {'name': <Berry name:str>, 'url': <Berry url:str>}
    """
    self._complete_berry_url_list += result_list
  
  def _fetch_element_growth_time_info(self, element: dict) -> dict:
    """
    Parameters
    ----------
    element : list
        Single berry url elements with format {'name': <Berry name:str>, 'url': <Berry url:str>}
    """
    response = requests.get(element['url'])
    response = response.json()
    return response['growth_time']
  
  def fetch_stats(self, element_limit: int = 20) -> None:
    """
    Parameters
    ----------
    element_limit : int
        Number of Berry elements to fetch in each iteration
    """
    next_url = self._base_url
    while next_url:
      response = requests.get(next_url, params={"limit": element_limit})
      response = response.json()
      self._add_elements_from_list(response['results'])
      next_url = response['next']
    # Now fetch each element growth info from its url
    self._berry_growth_times = np.array([self._fetch_element_growth_time_info(element) for element in self._complete_berry_url_list])
    self._berry_names = [element['name'] for element in self._complete_berry_url_list]
  
  def calculate_stats(self) -> dict:
    """
    Parameters
    ----------
    """
    berries_names = self._berry_names
    min_growth_time = np.min(self._berry_growth_times).item()
    median_growth_time = round(np.median(self._berry_growth_times),1).item()
    max_growth_time = np.max(self._berry_growth_times).item()
    variance_growth_time = round(np.var(self._berry_growth_times),1).item()
    mean_growth_time = round(np.mean(self._berry_growth_times),1).item()
    unique, counts = np.unique(self._berry_growth_times, return_counts=True)
    frequency_growth_time = dict(zip(unique.tolist(), counts.tolist()))
    res = {
      "berries_names": berries_names,
      "min_growth_time": min_growth_time,
      "median_growth_time": median_growth_time,
      "max_growth_time": max_growth_time,
      "variance_growth_time": variance_growth_time,
      "mean_growth_time": mean_growth_time,
      "frequency_growth_time": frequency_growth_time,
    }
    return res
  
  def generate_histogram_image(self) -> str:
    try:
      chart = sns.histplot(data=stats_dict['frequency_growth_time'])
      chart.set_title('Berry Growth Time Histogram', fontdict={'size': 20})
      chart.set_xlabel('Time')
      target_path = './assets/hist.png'
      os.makedirs(os.path.dirname(target_path),exist_ok=True)
      chart.get_figure().savefig(target_path)
      return target_path
    except Exception as e:
      print("Error while generating histogram: ", e)
      return None
