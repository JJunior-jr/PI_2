from io import BytesIO
import base64
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator


def graph(x_or_values, y_or_label, type) :
    fig = Figure()
    ax = fig.subplots()

    if type == "pie":
        labels = y_or_label
        sizes = x_or_values
        ax.pie(sizes, labels=labels)
        ax.legend()
    else:
        fig.subplots_adjust(left=0.06, right=0.95, top=0.95, bottom=0.06, hspace=0.3)
        ax.plot(x_or_values, y_or_label)
        ax.xaxis.set_major_locator(MaxNLocator(nbins=10))

    buf = BytesIO()
    fig.savefig(buf, format="svg")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    value = f"data:image/svg+xml;base64,{data}"

    return value