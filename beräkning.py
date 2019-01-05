"""import ekvationer as ekv
import enhet


class ULSTrä(ekv.SS_EN_1995_1_1, enhet.enhet):
    def __init__(self):
        super().__init__()

        self.beräkna()

    def beräkna(self):
        resultat = []

        resultat.append(("slankhet pelare", self.slankhet_pelare_kompression()))

        resultat.append(("slankhet balk", self.slankhet_balk_böj()))

        #TODO tryck_90

        if self.N == 0:
            resultat.append(("böjning", self.böjning()))
        elif self.N > 0:
            resultat.append(("böjning+drag", self.böjning_och_drag()))
        elif self.N < 0:
            resultat.append(("böjning+tryck", self.böjning_och_tryck()))

        if self.V != 0:
            resultat.append(("tvärkraft", self.tvärkraft()))

        if self.T != 0:
            resultat.append(("vridning", self.vridning()))

        #TODO kompression i vinkel

        return "id: {}".format(self.id), resultat

    # 1 Stress one direction ===============

    # 6.1.2
    def drag_0(self):
        res_6_1 = self.ekv_6_1()

        return res_6_1

    # 6.1.3
    def drag_90(self):
        pass

    # 6.1.4
    def tryck_0(self):
        res_6_2 = self.ekv_6_2()

        #TODO lägg in modul för stabilitet (6.3.2), om column

        return res_6_2

    # 6.1.5
    def tryck_90(self):
        res_6_3 = self.ekv_6_3()

        #TODO lägg in modul för stabilitet (6.3.2), om column


        return res_6_3

    # 6.1.6
    def böjning(self):
        res_6_11 = self.ekv_6_11()
        res_6_12 = self.ekv_6_12()

        #TODO lägg in modul för stabilitet (6.3.3), om beam

        return res_6_11, res_6_12

    # 6.1.7
    def tvärkraft(self):
        #TODO tvärkrfaft verkar vara fel
        res_6_13 = self.ekv_6_13()

        return res_6_13

    # 6.1.8
    def vridning(self):
        res_6_14 = self.ekv_6_14()

        return res_6_14

    # 2 Combined stresses ===================

    # 6.2.2
    def kompression_i_vinkel(self):
        #TODO lägg in modul för stabilitet (6.3.2), om column

        pass

    # 6.2.3
    def böjning_och_drag(self):
        res_6_17 = self.ekv_6_17()
        res_6_18 = self.ekv_6_18()

        #TODO lägg in modul för stabilitet (6.3.3), om beam

        return res_6_17, res_6_18

    # 6.2.4
    def böjning_och_tryck(self):
        res_6_19 = self.ekv_6_19()
        res_6_20 = self.ekv_6_20()

        #TODO lägg in modul för stabilitet (6.3.2), om column
        #TODO lägg in modul för stabilitet (6.3.3), om beam

        return res_6_19, res_6_20

    # 3 Stability of members ================

    # 6.3.2
    def slankhet_pelare_kompression(self):
        self.lambda_rel_y = self.ekv_6_21()
        self.lambda_rel_z = self.ekv_6_22()

        if self.lambda_rel_z <= 0.3 and self.lambda_rel_y <= 0.3:
            res_1 = self.ekv_6_19()
            res_2 = self.ekv_6_20()
        else:
            res_1 = self.ekv_6_23()
            res_2 = self.ekv_6_24()


        return res_1, res_2

    # 6.3.3
    def slankhet_balk_böj(self):
        if self.M_z > 0 and self.N == 0 and self.M_y == 0: #TODO är det verkligen M_Y? inte bara N?
            return self.ekv_6_33() #TODO värde return
        elif self.M_z > 0 and self.N < 0 and self.M_y == 0:
            return self.ekv_6_35()

    # 4 Varying cross-section or curved shape

    # 5 Notched beams =======================

    # 6 System Strength =====================


if __name__ == "__main__":
    ber = ULSTrä()
    print(ber.beräkna())"""
