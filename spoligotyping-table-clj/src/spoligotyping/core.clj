(ns spoligotyping.core
  (:require [hickory.core :as hc]
            [clojure.string :as str]
            [clojure.java.io :as io]
            [clojure.data.csv :as csv]))


(def spoligo-data (let [spoligo-vector (-> "resources/spoligo_table.html"
                                           slurp
                                           hc/parse
                                           hc/as-hiccup
                                           second
                                           (nth 4))]
                    (->> spoligo-vector
                         (drop 5)
                         (remove (fn [y] (= "\n" y)))
                         (map (fn [x] (if (string? x)
                                        (-> x
                                          (str/trim )
                                          (str/replace  #"\n" "_")))))
                         (remove nil?))))


(let [csv-headers (cons "0" (take 44 spoligo-data))
      csv-columns (partition 45 (drop 44 spoligo-data))
      csv-data (cons csv-headers csv-columns)]
  (with-open [writer (io/writer "resources/output.csv")]
    (csv/write-csv writer
                   csv-data)))




