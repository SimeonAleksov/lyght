import click


def call_click_command(cmd, *args, **kwargs):
    """
    Wrapper to call a click command
    """

    arg_values = {c.name: a for a, c in zip(args, cmd.params)}
    args_needed = {c.name: c for c in cmd.params
                   if c.name not in arg_values}

    opts = {a.name: a for a in cmd.params if isinstance(a, click.Option)}
    for name in kwargs:
        if name in opts:
            arg_values[name] = kwargs[name]
        else:
            if name in args_needed:
                arg_values[name] = kwargs[name]
                del args_needed[name]
            else:
                raise click.BadParameter(
                    "Unknown keyword argument '{}'".format(name))


    for arg in (a for a in cmd.params if isinstance(a, click.Argument)):
        if arg.name not in arg_values:
            raise click.BadParameter("Missing required positional"
                                     "parameter '{}'".format(arg.name))

    opts_list = sum(
        [[o.opts[0], str(arg_values[n])] for n, o in opts.items()], [])
    args_list = [str(v) for n, v in arg_values.items() if n not in opts]
    cmd(opts_list + args_list)


@click.command(context_settings=dict(allow_extra_args=True))
@click.option("--command", "-c")
@click.pass_context
def exec_command(ctx, command):
    from lyght.commands.generic.init import init

    print(ctx.args)
    commands = {
        'init': init,
    }
    cmnd_to_execute = commands.get(command)
    if cmnd_to_execute is not None:
        call_click_command(cmnd_to_execute)


if __name__ == "__main__":
    exec_command()
