"""
Package containing all classes of objects found at Wairakei geothermal field
"""

class Well:
    """
    Generic well
    """
    def __init__(self, mf_regression, enthalpy_dist, whp=None, flows_to=[], name="Unnamed well"):
        self.mf_regression = mf_regression          # regression model mf ~ whp
        self.enthalpy_dist = enthalpy_dist        # distribution of steam output
        self.flows_to = flows_to        # objects to pass steam to
        self.name = name

    def __repr__(self):
        repr = "<Well '%s', h: %.2f>" % (self.name, self.enthalpy)
        return repr

    def rsample(size, whp=None):
        """
        Take n samples from the well's full conditional
        """
        if whp is None:
            if self.whp is None:
                raise ValueError("whp not specified")
            else:
                whp = self.whp

        enthalpy = self.enthalpy_dist.rvs(size)
        mass_flow = mf_regression.predict(whp)
        return enthalpy, mass_flow


class Pipe:
    """
    Generic pipe
    """
    def __init__(self, flows_from=[], flows_to=[], name="Unnamed pipe"):
        self.flows_from = flows_from    # objects to accept steam from
        self.flows_to = flows_to        # objects to pass steam to
        self.name = name

    def __repr__(self):
        repr = "<Pipe '%s'>" % self.name
        return repr


class Separator:
    """
    Generic separator
    """
    def __init__(self, flows_from=[], flows_to=[], name="Unnamed separator"):
        self.flows_from = flows_from    # objects to accept steam from
        self.flows_to = flows_to        # objects to pass steam to
        self.name = name

    def __repr__(self):
        repr = "<Separator '%s'>" % self.name
        return repr

class Generator:
    """
    Generic generator
    """
    def __init__(self, flows_from=[], flows_to=[], name="Unnamed generator"):
        self.flows_from = flows_from    # objects to accept steam from
        self.flows_to = flows_to        # objects to pass steam to
        self.name = name
