import { React, useState } from 'react'
import { useFilters, useSortBy, useTable } from "react-table";

import './Table.css'

export default function MyTable({ columns, data }) {
    const {
        getTableProps,
        getTableBodyProps,
        headerGroups,
        rows,
        prepareRow,
        setFilter,
    } = useTable({
        columns,
        data
    },
        useFilters,
        useSortBy
    );

    const [filterInput, setFilterInput] = useState("");

    const handleFilterChange = e => {
        const value = e.target.value || undefined;
        setFilter(3, value); // 2 is the column id for diseases
        setFilterInput(value);
    };


    return (
        <div className="container">
            <input
                value={filterInput}
                onChange={handleFilterChange}
                placeholder={"Search Diseases"}
                className="Filter"
            />
            <table {...getTableProps()} className="Table">
                <thead>
                    {headerGroups.map(headerGroup => (
                        <tr {...headerGroup.getHeaderGroupProps()} className="HeaderRow">
                            {headerGroup.headers.map(column => (
                                <th {...column.getHeaderProps(column.getSortByToggleProps())} className="HeaderCell">{column.render("Header")}</th>
                            ))}
                        </tr>
                    ))}
                </thead>
                <tbody {...getTableBodyProps()}>
                    {rows.map((row, i) => {
                        prepareRow(row);
                        return (
                            <tr {...row.getRowProps()} className="Row">
                                {row.cells.map(cell => {
                                    return <td {...cell.getCellProps()} className="Cell">{cell.render("Cell")}</td>;
                                })}
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    );
}