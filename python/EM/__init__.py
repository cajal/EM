import datajoint as dj
import random
import itertools
import numpy as np

schema = dj.schema('seunglab_em', locals())


@schema
class Stack(dj.Manual):
    definition = """
    # EM Stack

    em              : smallint unsigned    # Seung Lab stack identifier
    ---
    boss_stack_id   : char(16)             # ID in the BOSS
    """


@schema
class VoxelSet(dj.Manual):
    definition = """
    # region in the stack

    -> Stack
    ---
    boss_vset_id     : char(16)
    """


@schema
class KeyPoint(dj.Manual):
    definition = """ # appproximate centroid of the neuron's centroid
    -> VoxelSet
    ---
    x : double  # (um) -- EM scan coordinate system
    y : double  # (um)
    z : double  # (um)
    """

    def generate_dummy_data(self):
        for neuron in Neuron().fetch.as_dict():
            neuron['x'], neuron['y'], neuron['z'] = np.random.rand(3) * 1000
            self.insert1(neuron)


@schema
class BoundingBox(dj.Manual):
    definition = """
    # Bounding box of fragments -- what can have a bounding box?
    -> VoxelSet
    ----
    x1      : float # (um)
    y1      : float # (um)
    z1      : float # (um)
    x2      : float # (um)
    y2      : float # (um)
    z2      : float # (um)
    """


@schema
class Neuron(dj.Manual):
    definition = """
    #  anatomically identified neurons

    -> Stack
    neuron_id   : int  unsigned           # Seung Lab neuron identifier
    ---
    -> VoxelSet
    """


@schema
class Synapse(dj.Manual):
    definition = """
    # synapse between two neurons

    synapse_id          : int unsigned # unique identifier of
    -> Stack
    ---
    pre -> Neuron
    post -> Neuron
    -> VoxelSet
    """

