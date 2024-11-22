def unnest_multi(df, columns, reset_index=False):
# expands out columns of lists into 1d, as well as
# duplicating other non-specified rows as needed.
# all the lists must be the same length across columns in a given row, but
# can vary between rows
# adapted from https://stackoverflow.com/questions/21160134/flatten-a-column-with-value-of-type-list-while-duplicating-the-other-columns-va
    '''
    df_flat = pd.DataFrame(columns=columns)
    print("df_flat")
    print(df_flat[df_flat.index.duplicated()])
    print("")
    for col in columns:
        col_flat = pd.DataFrame([[i, x] 
                       for i, y in df[col].apply(list).iteritems() 
                           for x in y], columns=['I', col])
        print("whole col flat")
        print(col_flat)
        #col_flat = col_flat.set_index('I')
        print("")
        print("col_flat duplications")
        print(col_flat[col_flat.index.duplicated()])
        df_flat[col] = col_flat
    df = df.drop(labels=columns, axis=1)
    df = df.merge(df_flat, left_index=True, right_index=True)
        '''
    df = df.explode(columns, ignore_index=False)
    if reset_index:
        df = df.reset_index(drop=True)
    return df