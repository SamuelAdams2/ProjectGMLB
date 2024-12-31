from django.shortcuts import render
import requests

# Create your views here.
def hello_world(request):
    return render(request, 'HTML/hello_world.html') # Refer to parent folder than file name. I.E. CSS/Filename.css

def get_game_data(request, game_id):
  """
  Fetches live game data from GUMBO API for a given game ID.

  Args:
      request: Django HTTP request object.
      game_id: The ID of the game to fetch data for.

  Returns:
      A Django HTTP response object with the game data or an error message.
  """

  # Replace with your desired endpoint URL (e.g., current game state)
  url = f"https://statsapi.mlb.com/api/v1.1/game/{game_id}/feed/live"

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    game_data = response.json()
    return render(request, 'game_data.html', {'game_data': game_data})
  except requests.exceptions.RequestException as e:
    error_message = f"Error fetching game data: {e}"
    return render(request, 'game_data.html', {'error_message': error_message})