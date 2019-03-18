from abc import ABC, abstractmethod

class Validation(ABC):
	@abstractmethod
	def validate(self, input_text):
		pass