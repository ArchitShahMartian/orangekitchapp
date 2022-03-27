import * as React from "react";
import {
    H6,
    Card,
    Button,
    Navbar,
    NavbarHeading,
    NavbarGroup,
    NavbarDivider,
    Menu,
    MenuItem } from "@blueprintjs/core";
import {
    Table,
    Column,
    Cell,
    Utils,
    ColumnHeaderCell } from "@blueprintjs/table";
import { Popover2 } from "@blueprintjs/popover2";
import { Inventory } from "../services/api/Inventory.ts"

interface IDashboardState {
    productList?: any
}

export interface ISortableColumn {
    getColumn(getCellData: ICellLookup, sortColumn: ISortCallback): JSX.Element;
}

abstract class AbstractSortableColumn implements ISortableColumn {
    constructor(protected name: string, protected index: number) {}

    public getColumn(getCellData: ICellLookup, sortColumn: ISortCallback) {
        const cellRenderer = (rowIndex: number, columnIndex: number) => (
            <Cell>{getCellData(rowIndex, columnIndex)}</Cell>
        );
        const menuRenderer = this.renderMenu.bind(this, sortColumn);
        const columnHeaderCellRenderer = () => <ColumnHeaderCell name={this.name} menuRenderer={menuRenderer} />;
        return (
            <Column
                cellRenderer={cellRenderer}
                columnHeaderCellRenderer={columnHeaderCellRenderer}
                key={this.index}
                name={this.name}
            />
        );
    }

    protected abstract renderMenu(sortColumn: ISortCallback): JSX.Element;
}

class TextSortableColumn extends AbstractSortableColumn {
    protected renderMenu(sortColumn: ISortCallback) {
        const sortAsc = () => sortColumn(this.index, (a, b) => this.compare(a, b));
        const sortDesc = () => sortColumn(this.index, (a, b) => this.compare(b, a));
        return (
            <Menu>
                <MenuItem icon="sort-asc" onClick={sortAsc} text="Sort Asc" />
                <MenuItem icon="sort-desc" onClick={sortDesc} text="Sort Desc" />
            </Menu>
        );
    }
        private compare(a: any, b: any) {
        return a.toString().localeCompare(b);
    }
}


export class Dashboard extends React.Component<IDashboardState> {
    constructor(props){
        super(props);
        this.state = {
            columns: [
                new TextSortableColumn("Product List", 0),
                new TextSortableColumn("Size", 1),
                new TextSortableColumn("Price", 2),
                new TextSortableColumn("Quantity in Stock", 3),
                new TextSortableColumn("Material", 4),
            ] as ISortableColumn[],
            productList: [],
            sortedIndexMap: [] as number[]
        }
        this.getProductList = this.getProductList.bind(this)
    }

    render(){
        const columns = this.state.columns.map(col => col.getColumn(this.getCellData, this.sortColumn));
        return (
            <div className={"bp3-dark"}>
                <Navbar>
                    <NavbarGroup>
                        <NavbarHeading>Orange Kitch</NavbarHeading>
                    </NavbarGroup>
                    <NavbarGroup className={"bp3-align-right"}>
                        <Popover2 inheritDarkTheme={true}
                          content={
                              <Card>
                                  <div className="container">
                                      <H6>Product List</H6>
                                  </div>
                                  <div>
                                        <Table
                                            numRows={this.state.productList.length}
                                            className={"bp4-dark"}>
                                            {columns}
                                        </Table>
                                  </div>
                              </Card>
                          }>
                          <Button>Product Info</Button>
                        </Popover2>
                    </NavbarGroup>
                </Navbar>
            </div>
        )
    }

    componentDidMount(){
        Promise.all([
            this.getProductList()]
        )
    }

    private getCellData = (rowIndex: number, columnIndex: number) => {
        const sortedRowIndex = this.state.sortedIndexMap[rowIndex];
        if (sortedRowIndex != null){
            rowIndex = sortedRowIndex
        }
        return this.state.productList[rowIndex][columnIndex]
    }

    private sortColumn = (columnIndex: number, comparator: (a: any, b: any) => number) =>{
        const { data } = this.state;
        const sortedIndexMap = Utils.times(data.length, (i: number) => i);
        sortedIndexMap.sort((a: number, b: number) =>{
            return comparator(data[a][columnIndex], data[b][columnIndex]);
        });
        this.setState({sortedIndexMap});
    }

    getProductList = () => {
        Inventory.list().then((response: any) => {
            this.setState({
                productList: response.data.data
            });
        })
    }
}