from .abstract_data_types import AbstractSlicableDynamicArray
from .dynamic_array import _BaseDynamicArray


class SlicableDynamicArray(_BaseDynamicArray, AbstractSlicableDynamicArray):

    def __getitem__(self, i: int or slice) -> object or tuple:
        item_or_slice = super().__getitem__(i)
        if isinstance(i, slice):
            resolved_slice = None
            try:
                capacity = self.get_capacity()
                resolved_slice = slice(*i.indices(capacity))
            except TypeError as e:
                pass

            if resolved_slice:
                correct_bounds = (self._check_start_ind_bounds(resolved_slice.start)
                                  and self._check_stop_ind_bounds(resolved_slice.stop))
                if correct_bounds:

                    item_or_slice = tuple(self.__array[resolved_slice])

                    self.__getitem_status = self.GETITEM_SLICE_OK
                else:

                    item_or_slice = ()

            elif not resolved_slice:
                self.__getitem_status = self.GETITEM_SLICE_TYPE_ERR
        else:

            item_or_slice = super()[i]

        return item_or_slice

    def _check_stop_ind_bounds(self, i: int) -> bool:
        return 0 <= i <= len(self)

