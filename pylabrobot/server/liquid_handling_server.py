""" Needs some refactoring. """
# mypy: disable-error-code = attr-defined

import asyncio
import json
import os
import threading
from typing import Any, Coroutine, List, Tuple, Type, TypeVar, Optional, cast

from flask import Blueprint, Flask, request, jsonify, current_app
from flask_cors import CORS, cross_origin
import werkzeug

from pylabrobot.liquid_handling import LiquidHandler
from pylabrobot.liquid_handling.backends import LiquidHandlerBackend
from pylabrobot.liquid_handling.standard import PipettingOp, Pickup, Aspiration, Dispense, Drop, Move
from pylabrobot.resources import Coordinate, Deck, Tip, Liquid, TecanTip400
from pylabrobot.serializer import serialize, deserialize
import usb.backend.libusb0 as libusb0

lh_api = Blueprint("liquid handling", __name__)


class Task:
  """ A task is a coroutine that runs in a separate thread. Maintains its own event loop and
  status. """

  def __init__(self, co: Coroutine[Any, Any, None]):
    self.status = "queued"
    self.co = co
    self.error: Optional[str] = None

  def run_in_thread(self) -> None:
    """ Run the coroutine in a new thread. """
    def runner():
      self.status = "running"
      loop = asyncio.new_event_loop()
      asyncio.set_event_loop(loop)
      try:
        loop.run_until_complete(self.co)
      except Exception as e: # pylint: disable=broad-except
        self.error = str(e)
        self.status = "error"
      else:
        self.status = "succeeded"

    t = threading.Thread(target=runner)
    t.start()

  def serialize(self, id_: int) -> dict:
    d = {"id": id_, "status": self.status}
    if self.error is not None:
      d["error"] = self.error
    return d

tasks: List[Task] = []

def add_and_run_task(task: Task):
  id_ = len(tasks)
  tasks.append(task)
  task.run_in_thread()
  return task.serialize(id_)


@lh_api.route("/")
def index():
  return "PLR Liquid Handling API"


@lh_api.route("/tasks", methods=["GET"])
def get_tasks():
  return jsonify([{"id": i, "status": t.status} for i, t in enumerate(tasks)])

@lh_api.route("/tasks/<int:id_>", methods=["GET"])
def get_task(id_: int):
  if id_ >= len(tasks):
    return jsonify({"error": "task not found"}), 404
  return tasks[id_].serialize(id_)


@lh_api.route("/setup", methods=["POST"])
async def setup():
  return add_and_run_task(Task(current_app.lh.setup()))

@lh_api.route("/stop", methods=["POST"])
async def stop():
  return add_and_run_task(Task(current_app.lh.stop()))

@lh_api.route("/status", methods=["GET"])
def get_status():
  status = "running" if current_app.lh.setup_finished else "stopped"
  return jsonify({"status": status})


@lh_api.route("/move_plate", methods=["POST"])
async def move_plate():

  data = request.get_json()

  resource_name = data["resource_name"]
  to = data["to"]
  resource = current_app.lh.deck.get_resource(resource_name)
  resource_to = current_app.lh.deck.get_resource(to)

  return add_and_run_task(Task(current_app.lh.move_plate(resource, resource_to)))


@lh_api.route("/rinse", methods=["POST"])
async def rinse_tips():


  await current_app.lh.backend._park_liha()
  # await self.liha.initialize_plunger(self._bin_use_channels(list(range(self.num_channels))))
  await current_app.lh.backend.liha.position_valve_logical([1] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.move_plunger_relative([100] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_valve_logical([0] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.set_end_speed_plunger([1800] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.move_plunger_relative([-100] * current_app.lh.backend.num_channels)

  await current_app.lh.backend.liha.position_valve_logical([1] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.move_plunger_relative([100] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_valve_logical([0] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.set_end_speed_plunger([1800] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.move_plunger_relative([-100] * current_app.lh.backend.num_channels)


  await current_app.lh.backend.liha.position_valve_logical([1] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.move_plunger_relative([100] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_valve_logical([0] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.set_end_speed_plunger([1800] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.move_plunger_relative([-100] * current_app.lh.backend.num_channels)


  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 120, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 120, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 120, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)


  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range-150] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range-150] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range-150] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range-150] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range-150] * current_app.lh.backend.num_channels)
  await current_app.lh.backend.liha.position_absolute_all_axis(45, 1031, 90, [current_app.lh.backend._z_range] * current_app.lh.backend.num_channels)


  return add_and_run_task(Task(current_app.lh.rinse_tips()))


@lh_api.route("/layout", methods=["GET"])
def get_layout():
  """ API Endpoint to inspect the current design of the deck
  Bo 20230912 """
  layout = current_app.lh.deck.serialize()
  return jsonify({"layout": layout})

@lh_api.route("/update_head_state", methods=["POST"])
def update_head_state():
  """ API Endpoint to update liquid handler head.
  Useful for TECAN with non-reuable tips.
  TO DO: Pass tip type as parameter
  Bo 20230912 """

  current_app.lh.clear_head_state()
  current_app.lh.update_head_state({0:TecanTip400()})
  current_app.lh.update_head_state({1:TecanTip400()})
  current_app.lh.update_head_state({2:TecanTip400()})
  current_app.lh.update_head_state({3:TecanTip400()})
  current_app.lh.update_head_state({4:TecanTip400()})
  current_app.lh.update_head_state({5:TecanTip400()})
  current_app.lh.update_head_state({6:TecanTip400()})
  current_app.lh.update_head_state({7:TecanTip400()})

  result = True

  return jsonify({"result": result})

@lh_api.route("/labware", methods=["POST"])
def define_labware():
  try:
    data = request.get_json()
    if not isinstance(data, dict):
      raise werkzeug.exceptions.BadRequest
  except werkzeug.exceptions.BadRequest:
    return jsonify({"error": "json data must be a dict"}), 400

  try:
    print(data["deck"])
    deck = Deck.deserialize(data=data["deck"])
    current_app.lh.deck = deck
  except KeyError as e:
    return jsonify({"error": "missing key in json data: " + str(e)}), 400

  return jsonify({"status": "ok"})

class ErrorResponse(Exception):
  def __init__(self, data: dict, status_code: int):
    self.data = data
    self.status_code = status_code


@lh_api.route("/pick-up-tips", methods=["POST"])
async def pick_up_tips():
  try:
    data = request.get_json()
    pickups = []
    for sc in data["channels"]:
      try:
        resource = current_app.lh.deck.get_resource(sc["resource_name"])
      except ValueError as exc:
        raise ErrorResponse({"error": f"resource with name '{sc['resource_name']}' not found"},
                            404) from exc
      if not "tip" in sc:
        raise ErrorResponse({"error": "missing key in json data: tip"}, 400)
      tip = cast(Tip, deserialize(sc["tip"]))
      if not "offset" in sc:
        raise ErrorResponse({"error": "missing key in json data: offset"}, 400)
      offset = cast(Coordinate, deserialize(sc["offset"]))
      pickups.append(Pickup(resource=resource, tip=tip, offset=offset))
    use_channels = data["use_channels"]
  except ErrorResponse as e:
    return jsonify(e.data), e.status_code

  return add_and_run_task(Task(current_app.lh.pick_up_tips(
    tip_spots=[p.resource for p in pickups],
    offsets=[p.offset for p in pickups],
    use_channels=use_channels
  )))

@lh_api.route("/drop-tips", methods=["POST"])
async def drop_tips():
  try:
    data = request.get_json()
    drops = []
    for sc in data["channels"]:
      try:
        resource = current_app.lh.deck.get_resource(sc["resource_name"])
      except ValueError as exc:
        raise ErrorResponse({"error": f"resource with name '{sc['resource_name']}' not found"},
                            404) from exc
      if not "tip" in sc:
        raise ErrorResponse({"error": "missing key in json data: tip"}, 400)
      tip = cast(Tip, deserialize(sc["tip"]))
      if not "offset" in sc:
        raise ErrorResponse({"error": "missing key in json data: offset"}, 400)
      offset = cast(Coordinate, deserialize(sc["offset"]))
      drops.append(Drop(resource=resource, tip=tip, offset=offset))
    use_channels = data["use_channels"]
  except ErrorResponse as e:
    return jsonify(e.data), e.status_code

  return add_and_run_task(Task(current_app.lh.drop_tips(
    tip_spots=[d.resource for d in drops],
    offsets=[d.offset for d in drops],
    use_channels=use_channels
  )))

@lh_api.route("/aspirate", methods=["POST"])
async def aspirate():
  try:
    data = request.get_json()
    aspirations = []
    for sc in data["channels"]:
      try:
        resource = current_app.lh.deck.get_resource(sc["resource_name"])
      except ValueError as exc:
        raise ErrorResponse({"error": f"resource with name '{sc['resource_name']}' not found"},
                            404) from exc
      if not "tip" in sc:
        raise ErrorResponse({"error": "missing key in json data: tip"}, 400)
      tip = cast(Tip, deserialize(sc["tip"]))
      if not "offset" in sc:
        raise ErrorResponse({"error": "missing key in json data: offset"}, 400)
      offset = cast(Coordinate, deserialize(sc["offset"]))
      volume = sc["volume"]
      flow_rate = sc["flow_rate"]
      liquid_height = sc["liquid_height"]
      blow_out_air_volume = sc["blow_out_air_volume"]
      liquid = cast(Liquid, deserialize(sc["liquid"]))
      aspirations.append(Aspiration(resource=resource, tip=tip, offset=offset, volume=volume,
        flow_rate=flow_rate, liquid_height=liquid_height, blow_out_air_volume=blow_out_air_volume,
        liquid=liquid))
    use_channels = data["use_channels"]
  except ErrorResponse as e:
    return jsonify(e.data), e.status_code

  return add_and_run_task(Task(current_app.lh.aspirate(
    resources=[a.resource for a in aspirations],
    vols=[a.volume for a in aspirations],
    offsets=[a.offset for a in aspirations],
    flow_rates=[a.flow_rate for a in aspirations],
    use_channels=use_channels
  )))

@lh_api.route("/dispense", methods=["POST"])
async def dispense():
  try:
    data = request.get_json()
    dispenses = []
    for sc in data["channels"]:
      try:
        resource = current_app.lh.deck.get_resource(sc["resource_name"])
      except ValueError as exc:
        raise ErrorResponse({"error": f"resource with name '{sc['resource_name']}' not found"},
                            404) from exc
      if not "tip" in sc:
        raise ErrorResponse({"error": "missing key in json data: tip"}, 400)
      tip = cast(Tip, deserialize(sc["tip"]))
      if not "offset" in sc:
        raise ErrorResponse({"error": "missing key in json data: offset"}, 400)
      offset = cast(Coordinate, deserialize(sc["offset"]))
      volume = sc["volume"]
      flow_rate = sc["flow_rate"]
      liquid_height = sc["liquid_height"]
      blow_out_air_volume = sc["blow_out_air_volume"]
      liquid = cast(Liquid, deserialize(sc["liquid"]))
      dispenses.append(Dispense(resource=resource, tip=tip, offset=offset, volume=volume,
        flow_rate=flow_rate, liquid_height=liquid_height, blow_out_air_volume=blow_out_air_volume,
        liquid=liquid))
    use_channels = data["use_channels"]
  except ErrorResponse as e:
    return jsonify(e.data), e.status_code

  return add_and_run_task(Task(current_app.lh.dispense(
    resources=[d.resource for d in dispenses],
    vols=[d.volume for d in dispenses],
    offsets=[d.offset for d in dispenses],
    flow_rates=[d.flow_rate for d in dispenses],
    use_channels=use_channels
  )))


def create_app(lh: LiquidHandler):
  """ Create a Flask app with the given LiquidHandler """
  app = Flask(__name__)
  cors = CORS(app)
  app.lh = lh
  app.register_blueprint(lh_api)
  return app


def main():
  backend_file = os.environ.get("BACKEND_FILE", "backend.json")
  with open(backend_file, "r", encoding="utf-8") as f:
    data = json.load(f)
    backend = LiquidHandlerBackend.deserialize(data)

  deck_file = os.environ.get("DECK_FILE", "deck.json")
  with open(deck_file, "r", encoding="utf-8") as f:
    data = json.load(f)
    deck = Deck.deserialize(data)

  lh = LiquidHandler(backend=backend, deck=deck)

  app = create_app(lh)
  host = os.environ.get("HOST", "0.0.0.0")
  port = int(os.environ.get("PORT", 5001))
  app.run(debug=True, host=host, port=port)


if __name__ == "__main__":
  main()
