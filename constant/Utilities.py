from constant.Messages import Messages


class Utilities:
    @staticmethod
    def validate(data):
        errorMessages = []
        error = False
        for i in range(len(data)):
            value = list(data.values())[i]
            key = list(data.keys())[i]
            if (len(value) == 0 or value is None):
                errorMessages.append(Messages.CREDENTIAL_EMPTY.format(credential=key))
                error = True
                break
        return {
            'errorMessages': errorMessages,
            'error': error
        }

