from rasa_core.actions import Action
from rasa_core.events import SlotSet


class ActionGetBuildingDirections(Action):
    def name(self):
        # type: () -> Text
        return "actions.ActionGetBuildingDirections"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        return [SlotSet("matches", result if result is not None else [])]
