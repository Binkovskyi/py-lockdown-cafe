class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self):
        return "Visitor is not vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return "Visitor's vaccine is expired"


class NotWearingMaskError(Exception):
    def __str__(self):
        return "Visitor is not wearing a mask"



