import { useState } from "react"

interface selectionButtonInfo {
    title: string,
    description?: string,
    value: string,
}

function SelectionButton(
    {
        title,
        description,
        value,
        state,
        setState,
    } : {
        title: string,
        description?: string,
        value: string,
        state: string,
        setState: (newState: string) => void,
    }
) {
    return (
        <div 
            key={value}
            className={`${state == value ? 
                " bg-primary-100 p-4 outline outline-primary-600 rounded cursor-pointer" : 
                " p-4 outline outline-slate-400 rounded cursor-pointer"}`}
            onClick={() => setState(value)}>
                <h3 className={`leading-none text-lg font-semibold ${state == value ? " text-dark-200 "  : "text-slate-200"} `}>{title}</h3>
                {description && (<p className={` leading-tight pt-1 text-sm ${state == value ? " text-dark-200 "  : "text-slate-200"}`}>{description}</p>)}
        </div>
    )
}

export default function ButtonInput(
    {
        setState,
        options,
        cols
    } : {
        setState: (newState: string) => void,
        options: selectionButtonInfo[],
        cols?: "one" | "two" | "three" | "four"
    }
) {
    const [selection, setSelection] = useState("")

    const changeSelection = (newSelection: string) => {
        setSelection(newSelection)
        setState(newSelection)
    }

    const gridOptions = {
        one: "grid-cols-1",
        two: "grid-cols-2",
        three: "grid-cols-3",
        four: "grid-cols-4",
    }

    return (
        <div className={`grid ${!cols ? gridOptions["two"] : gridOptions[cols]} gap-4`}>
            {options.map((option) => (
                <SelectionButton 
                    value={option.value} 
                    title={option.title}
                    description={option.description}
                    state={selection} 
                    setState={changeSelection}/>
            ))}
        </div>
    )
}