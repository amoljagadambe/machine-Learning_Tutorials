import numpy


class ExampleSet(object):
    """
    Each example contains:
        A : transition probability matrix of size states x states (row stochastic)
        HS : The hidden states
        O : The observations (emissions)
        priors : starting probabilities of the hidden states
        B : emission probability matrix of size states x emissions (row stochastic)
        ES : sequence of emissions (observations)
    """

    @staticmethod
    def healthy_fever():
        """
        A patient can be normal, cold, or dizzy.
        Are these flu symptoms?
        """
        A = numpy.array([
            [0.7, 0.3],
            [0.4, 0.6]
        ])

        HS = ['Healthy', 'Flu']
        O = ["normal", "cold", "dizzy"]
        priors = [0.6, 0.4]

        B = numpy.array([
            [0.5, 0.4, 0.1],
            [0.1, 0.3, 0.6]
        ])

        ES = ["normal", "cold", "dizzy"]

        return [A, HS, O, priors, B, ES]

    @staticmethod
    def dna_coding():
        """
        H characterizes coding DNA while L characterizes non-coding DNA.
        DNA can have protiens A C G T
        """

        A = numpy.array([
            [0.5, 0.5],
            [0.6, 0.4]
        ])

        HS = ['H', 'L']
        O = ['A', 'C', 'G', 'T']
        priors = [0.5, 0.5]

        # states x observables (row stochastic)
        B = numpy.array([
            [0.2, 0.3, 0.3, 0.2],
            [0.3, 0.2, 0.2, 0.3]
        ])

        ES = ['G', 'G', 'C', 'A', 'C', 'T', 'G', 'A', 'A']

        return [A, HS, O, priors, B, ES]

    @staticmethod
    def happy_sad_robot():
        """
        A robot is happy or sad depending on what it saw on tv
        """
        A = numpy.array([
            [0.99, 0.01],
            [0.1, 0.9]
        ])

        HS = ['Sad', 'Happy']
        O = ['GoT', 'W', 'EEnD', 'BB']
        priors = [0.2, 0.8]

        # states x observables (row stochastic)
        B = numpy.array([
            [0.1, 0.3, 0.5, 0.1],
            [0.4, 0.4, 0.2, 0.0]
        ])

        ES = ['GoT', 'BB', 'EEnD']

        return [A, HS, O, priors, B, ES]

    @staticmethod
    def urn_pick():
        """
        You can pick a red, green, or blue ball from three urns.
        Which urns did you pick from?
        """
        A = numpy.array([
            [0.1, 0.4, 0.5],
            [0.6, 0.2, 0.2],
            [0.3, 0.4, 0.3]
        ])

        HS = ['Urn1', 'Urn2', 'Urn3']
        O = ['R', 'G', 'B']
        priors = [0.5, 0.3, 0.2]

        # states x observables (row stochastic)
        B = numpy.array([
            [0.3, 0.5, 0.2],
            [0.1, 0.4, 0.5],
            [0.6, 0.1, 0.3]
        ])

        ES = ['R', 'R', 'G', 'G', 'B', 'R', 'G', 'R']

        return [A, HS, O, priors, B, ES]

    @staticmethod
    def part_of_speech_tag_simple():
        """
        Tags the words in a sentence with
            Noun, Modal, Verb.
        These words are
            Mary, Jane, Will, Spot, Can, See, Pat.

        Notice the ambiguitity in Will, Spot, and Pat.
        """
        A = numpy.array([
            [1 / 9, 1 / 3, 1 / 9],
            [1 / 4, 0, 3 / 4],
            [1, 0, 0]
        ])

        HS = ['Noun', 'Modal', 'Verb']
        O = ['Mary', 'Jane', 'Will', 'Spot', 'Can', 'See', 'Pat']
        priors = [3 / 4, 1 / 4, 0]

        # observables x states (column stochastic)
        B = numpy.array([
            [4 / 9, 0, 0],
            [2 / 9, 0, 0],
            [1 / 9, 3 / 4, 0],
            [2 / 9, 0, 1 / 4],
            [0, 1 / 4, 0],
            [0, 0, 1 / 2],
            [0, 0, 1 / 4]
        ])

        B = B.T  # states x observables (row stochastic)
        ES = ['Jane', 'Will', 'Spot', 'Pat']  # Jane will spot Will.

        return [A, HS, O, priors, B, ES]